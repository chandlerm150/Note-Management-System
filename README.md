# Note Management System
 
## Background:
Healthy Huskies is a health organization at St. Cloud State University, and one of their responsibilities is to handle questions/requests from students via phone. The details of phone calls are handled by writing things down on sticky notes which often get lost and cluttered. Employees forget the details of the phone calls, and never call the user back to fulfill their request. Healthy Huskies has received many angry complaints from students for this very reason, and superiors have voiced their frustration with the current system.

## Objective:
Create an application that manages notes for phone calls. The application allows a user (Telephone operator) to write a note with the details of the request for each phone call and store it in a repository. Each note contains information about the phone call, such as the student who called and their request, the employee who wrote the note, who the note is intended for, etc.  The student and employee (telephone operator) recorded in each note are identified by their ID numbers, which are stored in a database. If a student or employee doesn't exist in the database they can be added. Once a note is created, it can be retrieved at a later time to review the contents of the note and mark it as complete once it has been dealt with.  Note: This application is proof of concept and will not be deployed at SCSU Healthy Huskies.

## Requirements
 - Python 3.x
 - sqlite3
 - Tkinter
 
## Installation 
1. Clone or download the repository
2. Install the above requirements
3. Run UserInterface.py 
4. Enter the login prompt with any username and the password 1234
5. You can now add, view, and complete notes as well as add new students and employees to the database. 

Note: The noteDB file contains the sqlite database and is already instantiated with a few instances of students, employees, and notes. Use any username at the login prompt and the password "1234". For creating new notes, the valid employee ID numbers are 999, 888, and 777. Valid student ID numbers are 111, 222, and 333. Alternatively, you can add new students and employees to the database from the GUI, and then use those IDs to create a new note. When adding a new student or employee to the database, the ID numbers will be checked for duplicates before adding them to ensure unique IDs. 
 
 
 ## Demo
![](NoteSystemDemo.gif)
 
