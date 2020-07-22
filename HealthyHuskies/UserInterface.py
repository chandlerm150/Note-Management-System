from tkinter import *
import NoteList
from functools import partial


#Creates a simple login screen
def loginScreen():

    # Creates window
    userPW = "1234"
    screen = Tk()
    w = 250
    h = 250
    x = int(midpointX - w/2)
    y = int(midpointY - h/2)
    screen.geometry("{}x{}+{}+{}".format(w,h,x,y))
    global username
    global username_entry
    username = StringVar()
    global inputPW
    inputPW = StringVar()

    # A welcome prompt
    Label(screen, text="Healthy Huskies Callback Notes \n").pack()

    # A request prompt for user name
    Label(screen, text="Name").pack()  # Makes a input field for username
    username_entry = Entry(screen, textvariable=username)
    username_entry.pack()

    # A request prompt for user password
    Label(screen, text="Password").pack()
    password_entry = Entry(screen, textvariable=inputPW)
    password_entry.pack()
    pwEntry = password_entry.get()

    # Input text field for passward
    Label(screen, text="").pack()
    Button(screen, text="Login", width=10, height=1, command=partial(loginButtonClicked,password_entry,userPW,screen,username_entry)).pack()

    screen.mainloop()

def loginButtonClicked(PwEntryObject, userPW, screen,usernameEntryObject):
    if PwEntryObject.get() == userPW:
        mainMenu(screen)
    else:
        Label(screen, text="Invalid username / password", fg="red", font=("calibri", 11)).pack()
        return


## Main menu
def mainMenu(root):
    root.destroy()
    notes = notelist.getAllNotes()
    screen = Tk()
    w = 600
    h = 500
    x = int(midpointX - w/2)
    y = int(midpointY - h/2)
    screen.geometry("{}x{}+{}+{}".format(w,h,x,y))
    screen.title("Main Menu")

    ##Create listbox add all note entries to it
    global listbox
    listbox = Listbox(screen, borderwidth=5, font='Courier', relief='groove', selectbackground='lightgrey', height=12)
    firstline = formatText("STUDENT NAME", "STUDENT ID", "NOTE ID")
    for n in notes:
        print("The student id for this note is ", n.sID)
        if(n.status==0):
            theStudent = notelist.getStudentInfo(n.sID)

            studentName = theStudent.firstname
            textline = formatText(studentName, str(n.sID), str(n.noteID))
            listbox.insert(END, textline)

    #Create text labels
    Label(screen, text="Active Notes", fg="black", font=("calibri", 15)).pack(anchor='n')
    Label(screen, text="Select the note you would like to view", fg="black", font=("calibri", 12)).pack(anchor='n')
    Label(screen, text="").pack(anchor='n')
    Label(screen, text="").pack(anchor='n')
    Label(screen, text="\t\t\t\t\t\t\t\t\t\t" + firstline, fg="black", font=("Courier", 12)).pack(anchor='n')
    listbox.pack(anchor='n')
    listbox.config(width=60)
    Label(screen, text=" ").pack(anchor='n')

    ##Create buttons. Each button hands control to the function specified in it's 'command' argument when pressed.
    Button(screen, text= "View selected note", width=20,height =1, pady=5,command = partial(viewActiveNote,screen)).pack(anchor='n')
    Label(screen, text=" ").pack(anchor='n')
    Button(screen, text="Create new note", width=20, height=1, pady=5,padx = 2, command=partial(createNote,screen)).pack(side=LEFT)
    Button(screen, text="Add Employee",  width=20, height=1, pady=5,padx = 2, command=partial(addEmployee,screen)).pack(side=LEFT)
    Button(screen, text="Add Student", width=20, height=1, pady=5, padx=2, command=partial(addStudent, screen)).pack(side=LEFT)
    Button(screen, text="View completed Notes", width=20, height=1, pady=5, padx=2, command=partial(viewCompleted, screen)).pack(side=LEFT)

    line = listbox.get(ANCHOR)
    screen.update_idletasks()
    screen.mainloop()

# View the details of the selected completed note
def viewCompleted(root):
    #Create window
    root.destroy()
    notes = notelist.getAllNotes()
    screen = Tk()
    screen.title("Completed Notes")
    w = 600
    h = 500
    x = int(midpointX - w/2)
    y = int(midpointY - h/2)
    screen.geometry("{}x{}+{}+{}".format(w,h,x,y))

    ##Create listbox add all completed notes to it
    global listbox
    listbox = Listbox(screen, borderwidth=5, font='Courier', relief='groove', selectbackground='lightgrey', height=12)
    firstline = formatText("STUDENT NAME", "STUDENT ID", "NOTE ID")
    for n in notes:
        if (n.status == 1):
            theStudent = notelist.getStudentInfo(n.sID)
            studentName = theStudent.firstname
            textline = formatText(studentName, str(n.sID), str(n.noteID))
            listbox.insert(END, textline)

    #Create labels and buttons
    Label(screen, text="Completed Notes", fg="black", font=("calibri", 15)).pack(anchor='n')
    Label(screen, text="Select the note you would like to view", fg="black", font=("calibri", 12)).pack(anchor='n')
    Label(screen, text="").pack(anchor='n')
    Label(screen, text="").pack(anchor='n')
    Label(screen, text="\t\t\t\t\t\t\t\t\t\t" + firstline, fg="black", font=("Courier", 12)).pack(anchor='n')
    listbox.pack(anchor='n')
    listbox.config(width=60)
    Label(screen, text=" ").pack(anchor='n')
    Label(screen, text=" ").pack(anchor='n')
    Button(screen, text="View selected note", width=20, height=1, pady=5,padx=30, command=partial(getCompletedAnchor, screen)).pack(side=RIGHT)
    Button(screen, text="Go back", width=20, height=1, pady=5, padx=10, command=partial(mainMenu, screen)).pack(side=RIGHT)
    line = listbox.get(ANCHOR)
    screen.update_idletasks()
    screen.mainloop()

#Formats the string to fit the Tkinter listbox
def formatText(StudentName, sID, nID):
    s = "                                                                                                              "
    s = s[:2] + str(StudentName) + s[2:]
    s = s[:20] + str(sID) + s[20:]
    s = s[:35] + str(nID) + s[35:]
    return(s)

# View the details of the selected active note
def viewActiveNote(root):
    try:
        line = listbox.get(ANCHOR)
        root.destroy()
        noteID = int(line[35:])
        theNote = notelist.getNote(noteID)
        theStudent = notelist.getStudentInfo(theNote.sID)
        theEmployee = notelist.getEmpInfo(theNote.eID)
        statusNum = theNote.status

        if(statusNum==0):
            status = "Incomplete"
        else:
            status = "Complete"

        #Create window and listbox to display note details
        screen = Tk()
        w = 800
        h = 400
        x = int(midpointX - w / 2)
        y = int(midpointY - h / 2)
        screen.geometry("{}x{}+{}+{}".format(w, h, x, y))

        screen.title("View Note")
        Label(screen, font=('arial',14,'bold'), pady=30, text="Student Note Details").pack(anchor='n')
        listbox2 = Listbox(screen, borderwidth=5,fg = 'black', font='Courier', relief='groove', selectbackground='lightgrey', height=12,width=80)
        listbox2.insert(END, "Student first name:   " + theStudent.firstname)
        listbox2.insert(END, "Student last:         " + theStudent.lastname)
        listbox2.insert(END, "Student ID:           " + str(theStudent.sID))
        listbox2.insert(END, "Student phone:        " + str(theStudent.phonenumber))
        listbox2.insert(END, "Student address:      " + theStudent.address)
        listbox2.insert(END, "Note ID:              " + str(theNote.noteID))
        listbox2.insert(END, "Reason for note:      " + theNote.reason)
        listbox2.insert(END, "Additional notes:     " + theNote.note)
        listbox2.insert(END, "Note is for:          " + theNote.forWho)
        listbox2.insert(END, "Note made by:         " + theEmployee.firstname + " " + theEmployee.lastname)
        listbox2.insert(END, "Employee ID:          " + str(theNote.eID))
        listbox2.insert(END, "Date created:         " + theNote.createdDate)
        listbox2.insert(END, "Status:               " + status )
        listbox2.pack(anchor='n')

        #Create buttons
        b1 = Button(screen, text='   Go Back   ',command = partial(mainMenu, screen))
        b1.pack(side=RIGHT, padx=5, pady=5)
        b2 = Button(screen, text='    Mark as complete    ', command = partial(markComplete,screen,theNote))
        b2.pack(side=RIGHT, padx=5, pady=5)
        screen.mainloop()

    except Exception:
        screen = Tk()
        w = 250
        h = 50
        x = int(midpointX - w / 2)
        y = int(midpointY - h / 2)
        screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
        Label(screen, text="Error: Please select a note!\n", fg='red',
              font=('arial', 12, 'bold')).pack(anchor='w')

        filler = Tk()
        mainMenu(filler)



##Retrieves the Tkinter object that contains the user selected line from the "View completed notes" page
def getCompletedAnchor(root):
    try:
        line = listbox.get(ANCHOR)
        root.destroy()
        noteID = int(line[35:])
        viewCompletedNote(noteID)
    except:
        screen = Tk()  # Declares it as a Tk GUI
        screen.geometry("250x50")  # The dimensions
        Label(screen, text="Error: Please select a note!\n", fg='red',
              font=('arial', 12, 'bold')).pack(anchor='w')

        filler = Tk()

        mainMenu(filler)

##Create note page
def createNote(root):
    global entries
    entries = []

    root.destroy()
    screen = Tk()
    w = 400
    h = 250
    x = int(midpointX - w/2)
    y = int(midpointY - h/2)
    screen.geometry("{}x{}+{}+{}".format(w,h,x,y))
    screen.title("Create Note")
    fields = ('Student ID', 'For Who', 'Reason', 'Notes', 'Employee ID')
    for field in fields:
        row = Frame(screen)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)

    b2 = Button(screen, text=' Create Note', command=processEntries)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b2 = Button(screen, text='    Clear    ', command = clearEntries)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b1 = Button(screen, text='   Go Back   ', command = partial(mainMenu, screen)).pack(side=RIGHT, padx=5, pady=5)

    screen.mainloop()

##Add employee page
def addEmployee(root):
    global empEntries
    empEntries = []
    root.destroy()

    screen = Tk()
    w = 400
    h = 150
    x = int(midpointX - w/2)
    y = int(midpointY - h/2)
    screen.geometry("{}x{}+{}+{}".format(w,h,x,y))
    fields = ("Employee ID", "First Name", "Last Name")
    screen.title("Add Employee")

    for field in fields:
        row = Frame(screen)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        empEntries.append(ent)

    b2 = Button(screen, text=' Add Employee', command=processEmps)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b2 = Button(screen, text='    Clear    ', command=clearEmpEntries)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b1 = Button(screen, text='   Go Back   ', command=partial(mainMenu, screen)).pack(side=RIGHT, padx=5, pady=5)

    screen.mainloop()

##Add student page
def addStudent(root):
    global studentEntries
    studentEntries = []
    root.destroy()

    screen = Tk()
    w = 400
    h = 250
    x = int(midpointX - w/2)
    y = int(midpointY - h/2)
    screen.geometry("{}x{}+{}+{}".format(w,h,x,y))
    screen.title("Add Student")
    fields = ("Student ID", "First Name", "Last Name", "Address", "Phone Number")
    for field in fields:
        row = Frame(screen)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        studentEntries.append(ent)

    b2 = Button(screen, text=' Add Student', command=processStudents)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b2 = Button(screen, text='    Clear    ', command=clearStudentEntries)
    b2.pack(side=RIGHT, padx=5, pady=5)
    b1 = Button(screen, text='   Go Back   ', command=partial(mainMenu, screen)).pack(side=RIGHT, padx=5, pady=5)

    screen.mainloop()

def processEmps():
    vals = []

    for e in empEntries:
        vals.append(e.get())

    clearEmpEntries()
    return notelist.addEmps(vals)

def clearEmpEntries():
    for e in empEntries:
        e.delete(0,END)

def processStudents():
    vals = []

    for s in studentEntries:
        vals.append(s.get())
    clearStudentEntries()
    return notelist.addStudents(vals)

def clearStudentEntries():
    for e in studentEntries:
        e.delete(0,END)

# Retrieve the values contained in Tkinter entries and attempt to add them to DB
def processEntries():
    vals = []
    for e in entries:
        vals.append(e.get())

    clearEntries()
    return notelist.addToDB(vals)

def clearEntries():
    for e in entries:
        e.delete(0,END)

## View completed note page
def viewCompletedNote(noteID):
    screen = Tk()
    screen.geometry("800x400")
    screen.title("View Note")

    theNote = notelist.getNote(noteID)
    statusNum = theNote.status
    dateString = theNote.createdDate

    if(statusNum==0):
        status = "Incomplete"
    else:
        status = "Complete"

    theStudent = notelist.getStudentInfo(theNote.sID)
    theEmployee = notelist.getEmpInfo(theNote.eID)

    Label(screen, font=('arial',14,'bold'), pady=30, text="Student Note Details").pack(anchor='n')
    listbox = Listbox(screen, borderwidth=5,fg = 'black', font='Courier', relief='groove', selectbackground='lightgrey', height=12,width=80)
    listbox.insert(END, "Student first name:   " + theStudent.firstname)
    listbox.insert(END, "Student last:         " + theStudent.lastname)
    listbox.insert(END, "Student ID:           " + str(theStudent.sID))
    listbox.insert(END, "Student phone:        " + str(theStudent.phonenumber))
    listbox.insert(END, "Student address:      " + theStudent.address)
    listbox.insert(END, "Note ID:              " + str(theNote.noteID))
    listbox.insert(END, "Reason for note:      " + theNote.reason)
    listbox.insert(END, "Additional notes:     " + theNote.note)
    listbox.insert(END, "Note is for:          " + theNote.forWho)
    listbox.insert(END, "Note made by:         " + theEmployee.firstname + " " + theEmployee.lastname)
    listbox.insert(END, "Employee ID:          " + str(theNote.eID))
    listbox.insert(END, "Date created:         " + dateString)
    listbox.insert(END, "Status:               " + status )
    listbox.pack(anchor='n')

    b1 = Button(screen, text='   Go Back   ',command = partial(viewCompleted, screen))
    b1.pack(side=RIGHT, padx=5, pady=5)

#Changes the status of the selected note to complete
def markComplete(root, note):
    #root.destroy()
    notelist.markAsComplete(note)
    mainMenu(root)

##Create global variables
def createGlobals():
    global entries
    entries = []
    global username
    global notelist
    notelist = NoteList.NoteList()
    global midpointX
    global midpointY
    root = Tk()
    midpointX = root.winfo_screenwidth() / 2
    midpointY = root.winfo_screenheight() / 2
    root.destroy()


createGlobals()
loginScreen()