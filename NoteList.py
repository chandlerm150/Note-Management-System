import sqlite3
import Note
from tkinter import *
import Student
import Employee
from datetime import date


class NoteList:
    def __init__(self):
        self.conn = sqlite3.connect('noteDB')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Student(Student_ID INTEGER PRIMARY KEY, First_Name TEXT,"
                         " Last_Name TEXT, Address TEXT, PHONE_NUMBER TEXT) ")

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Employee(Employee_ID INTEGER PRIMARY KEY, Employee_Lname TEXT,"
            " Employee_Fname TEXT)")

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS studentNotes(Note_ID INTEGER PRIMARY KEY, note TEXT,"
            " reason TEXT, for_who TEXT, student_id INTEGER,"
            "Employee_ID INTEGER,  status INTEGER, created_date TEXT)")
        self.conn.close()

    #Adds a note to the database
    def addToDB(self, vals):
        database = self.getDatabaseConnection()
        cursor = database.cursor()

        # Gets a new note ID
        uniqueID = self.newNoteID()
        theDate = date.today()

        # Checks to make sure student ID and employee ID are integers
        if (not (self.isInteger(vals[0]) and self.isInteger(vals[4]))):
            screen = Tk()
            w = 400
            h = 50
            x = int(800)
            y = int(400)
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Error: Please enter the ID as an integer!\n", fg='red',
                  font=('arial', 12, 'bold')).pack(anchor='w')
            return

        # Creates a note object with the provided values
        note = Note.callNote(vals[0], vals[1], vals[2], vals[3], vals[4])
        note.noteID = uniqueID
        note.status = 0     # Sets the note status to 0, which means note is incomplete
        note.createdDate = str(theDate)

        # Checks to ensure the provided IDs exist in database
        sExists = self.studentExists(note.sID)
        eExists = self.empExists(note.eID)
        sqlFormula = sqlFormula = "INSERT INTO studentNotes (student_id, for_who, reason, note, Employee_ID,Note_ID, status, created_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        noteValues = (note.sID, note.forWho, note.reason, note.note, note.eID, note.noteID, note.status, note.createdDate)

        if (sExists & eExists):
            try:
                cursor.execute(sqlFormula, noteValues)
                database.commit()
                screen = Tk()
                w = 300
                h = 50
                x = int(800)
                y = int(400)
                screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
                Label(screen, text="Note successfully added!\n", fg='green', font=('arial', 12, 'bold')).pack(
                    anchor='w')

            except:
                screen = Tk()
                w = 350
                h = 50
                x = int(800)
                y = int(400)
                screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
                Label(screen, text="Database exception: Unable to add note!\n", fg='red',
                      font=('arial', 12, 'bold')).pack(
                    anchor='w')
            finally:
                database.close()
        else:
            screen = Tk()
            w = 350
            h = 125
            x = int(800)
            y = int(400)
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            if (not sExists):
                Label(screen, text="Error: Invalid student ID, please try again!\n", fg='red',
                      font=('arial', 12, 'bold')).pack(anchor='w')
            if (not eExists):
                Label(screen, text="Error: Invalid employee ID, please try again!\n", fg='red',
                      font=('arial', 12, 'bold')).pack(anchor='w')

    # Adds an employee to the database
    def addEmps(self, vals):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        validID = self.isInteger(vals[0])

        if (not validID):
            screen = Tk()
            w = 450
            h = 75
            x = 800
            y = 400
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Error: Invalid Employee ID, please enter an integer!\n", fg='red',
                  font=('arial', 12, 'bold')).pack(anchor='w')
            return

        emp = Employee.Employee(vals[0], vals[1], vals[2])
        empValues = (emp.eID, emp.lastname, emp.firstname)
        sqlFormula = """INSERT INTO Employee (Employee_ID, Employee_Lname, Employee_Fname) VALUES (?, ?, ?) """

        try:
            cursor.execute(sqlFormula, empValues)
            database.commit()
            screen = Tk()
            w = 350
            h = 100
            x = 800
            y = 400
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Employee successfully added!\n", fg='green', font=('arial', 12, 'bold')).pack(
                anchor='w')
        except:
            screen = Tk()
            w = 450
            h = 75
            x = 800
            y = 400
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Error: That ID already exists!\n", fg='red',
                  font=('arial', 12, 'bold')).pack(anchor='w')
        finally:
            database.close()

    # Adds a student to the database
    def addStudents(self, vals):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        validID = self.isInteger(vals[0])

        if (not validID):
            screen = Tk()
            w = 450
            h = 75
            x = 800
            y = 400
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Error: Invalid Employee ID, please enter an integer!\n", fg='red',
                  font=('arial', 12, 'bold')).pack(anchor='w')
            return

        stu = Student.Student(vals[0], vals[1], vals[2], vals[3], vals[4])
        sqlFormula = "INSERT INTO Student (Student_ID, First_Name, Last_Name, Address, Phone_Number) VALUES (?, ?, ?, ?, ?)"
        stuValues = (stu.sID, stu.firstname, stu.lastname, stu.address, stu.phonenumber)

        try:
            cursor.execute(sqlFormula, stuValues)
            database.commit()
            screen = Tk()
            w = 350
            h = 100
            x = 800
            y = 400
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Student successfully added!\n", fg='green', font=('arial', 12, 'bold')).pack(
                anchor='w')

        except:
            screen = Tk()
            w = 450
            h = 75
            x = 800
            y = 400
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Error: That ID already exists!\n", fg='red',
                  font=('arial', 12, 'bold')).pack(anchor='w')
        finally:
            database.close()

    # Marks a note as complete by setting status = 1
    def markAsComplete(self, thenote):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        id = thenote.noteID
        sqlFormula = 'UPDATE studentNotes SET status = 1 WHERE Note_ID = ' + str(id)

        try:
            cursor.execute(sqlFormula)
            database.commit()
            screen = Tk()
            w = 200
            h = 50
            x = int(800)
            y = int(400)
            screen.geometry("{}x{}+{}+{}".format(w, h, x, y))
            Label(screen, text="Note completed!\n", fg='green', font=('arial', 12, 'bold')).pack(
                anchor='w')
        except:
            screen = Tk()
            screen.geometry("450x75")
            Label(screen, text="Database exception: Unable to mark as complete!\n", fg='red',
                  font=('arial', 12, 'bold')).pack(anchor='w')

    # Retrieves the note with the specified note ID from the database
    def getNote(self, noteID):
        database = self.getDatabaseConnection()
        cursor = database.cursor()

        try:
            cursor.execute("SELECT * FROM studentNotes")
            notevalues = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to select all from studentNotes", error)
        finally:
            database.close()

        # Loop through note rows until one is found with the given noteID, then make a note object using those values
        for n in notevalues:
            if (int(n[0]) == int(noteID)):
                theNote = Note.callNote(n[4], n[3], n[2], n[1], n[5])
                theNote.noteID = n[0]
                theNote.status = n[6]
                theNote.createdDate = n[7]

        try:
            return theNote
        except Exception as error:
            print("Failed to retrieve note from database ", error)

    # Retrieves all notes from the database
    def getAllNotes(self):
        allNotes = []
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        try:
            cursor.execute("SELECT * FROM studentNotes")
            notes = cursor.fetchall()
        except:
            print("Database exception: Unable to fetch notes")
        finally:
            database.close()

        for n in notes:
            note = Note.callNote(n[4], n[3], n[2], n[1], n[5])
            note.noteID = n[0]
            note.status = n[6]
            note.createdDate = n[7]
            allNotes.append(note)

        return allNotes

    def isInteger(self, num):
        isInt = True

        for c in num:
            if (not c.isdigit()):
                isInt = False

        return isInt

    # Verifies that a student with the provided ID exists
    def studentExists(self, sID):
        exists = False
        database = self.getDatabaseConnection()
        cursor = database.cursor()

        try:
            cursor.execute("SELECT Student_ID FROM Student")
            studentIDs = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to select student_id from Student", error)
        finally:
            database.close()

        for row in studentIDs:
            if row[0] == int(sID):
                exists = True
        return exists

    # Verifies that an employee with the provided ID exists
    def empExists(self, eID):
        exists = False
        database = self.getDatabaseConnection()
        cursor = database.cursor()

        try:
            cursor.execute("SELECT Employee_ID FROM Employee")
            empIDs = cursor.fetchall()

        except sqlite3.Error as error:
            print("Failed to Select Employee_ID from Employee", error)


        finally:
            database.close()

        for e in empIDs:
            if int(e[0]) == int(eID):
                exists = True
        return exists


    # Returns the database connection so functions can access database
    def getDatabaseConnection(self):
        self.conn = sqlite3.connect('noteDB')
        return self.conn

    # Generates an ID for new notes
    def newNoteID(self):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        id = 0

        try:
            cursor.execute("SELECT Note_ID FROM studentNotes")
            noteIDs = cursor.fetchall()
        except:
            print("Database exception: Unable to fetch note id")
        finally:
            database.close()

        for i in noteIDs:
            if int(i[0]) > int(id):
                (id) = int(i[0])
        return id + 1

    # Retrieves student details for the provided student ID
    def getStudentInfo(self, sID):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        sID = int(sID)

        try:
            cursor.execute("SELECT * FROM Student")
            students = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to retrieve student info from database", error)
        finally:
            database.close()

        for s in students:
            if int(s[0]) == sID:
                theStudent = Student.Student(sID, fname = s[1], lname = s[2], addr=s[3],
                                             pnum = s[4])
        try:
            return theStudent
        except:
            print("Error: Student not found exception. Check inside getStudentInfo()")

    # Retrieves employee details for the provided employee ID
    def getEmpInfo(self, eID):
        database = self.getDatabaseConnection()
        cursor = database.cursor()
        eID = int(eID)

        try:
            cursor.execute("SELECT * FROM Employee")
            employees = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to select from Employee", error)
        finally:
            database.close()

        for e in employees:
            if int(e[0]) == eID:
                theEmployee = Employee.Employee(eID, fname=e[2], lname=e[1])
        try:
            return theEmployee
        except:
            print("Error: Employee not found exception. Check inside getStudentInfo()")