# This is a to-do application intended to be used on the command line.
# This first iteration is merely a self-containing to-do program.
# Once the program ends, all information is lost.

# Created by Dakota Kim.

import sys
import sqlite3
import os
import time
from itertools import chain

pwd = os.getcwd() # Returns the current directory. I'll add some customization to this section later.
sql_file = pwd + "/my_todo.db"

def run():
    response = raw_input("Hello! Is this your first time creating a to-do list in the terminal?\t")
    # If this is first time, will run the createDB method to create a database to store tasks.
    if response.lower() == "yes":
        createDB()
    elif response.lower() == "no":
        choice_maker()

def createDB():
    print("Awesome! Let's get started")
    time.sleep(0.5)
    print("Your current directory is " + pwd)
    time.sleep(0.5)
    print("Keep track of this path! Your database will be created here!")
    sql_file = pwd + "/my_todo.db"
    connection = sqlite3.connect(sql_file)
    connection.text_factory = str
    c = connection.cursor()
    # We have connected a database file. If file doesn't already exist, this connection
    # will create it. The next step is to create a table.
    c.execute('''CREATE TABLE tasks(task TEXT, importance INTEGER)''')
    # Eventually I would like to have a way for users to sort by what is due soonest.
    # Perhaps a MM/DD/YYYY implementation. I'll do some research into that. :)
    connection.commit()
    connection.close()
    if raw_input("Want to add a task?\t").lower() == "yes":
        creator()
    else:
        choice_maker()

def choice_maker():
    # The manager method will allow the user to control the contents of their to-do list.
    # The user will select a number that corresponds to their desire. I will implement
    # a tracking system for the user to keep track of how many tasks they've completed
    # and which ones! I will also implement a sorting method for users to decide which
    # criteria they'd like to sort by. :)
    print("""What would you like to do?
                       1 = Add a new task
                       2 = Complete a task
                       3 = List all tasks
                       4 = Sort tasks!
                       5 = Leave program""")
    time.sleep(1.0)
    choice = raw_input("Enter the number that corresponds to your choice!\t")
    if (choice.isdigit()):
        if choice == "1":
            creator()
        elif choice == "2":
            complete()
        elif choice == "3":
            list()
        elif choice == "4":
            sort()
        elif choice == "5":
            sys.exit()
        else:
            print ("You didn't enter a valid choice! Select a choice ranging from 1 to 5!")
            choice_maker()
    else:
        print("You didn't enter a valid number. :( No problem! We can start all over again! :D")
        choice_maker()

def creator(): # Method used to create new tasks for the list.
    connection = sqlite3.connect(sql_file)
    connection.text_factory = str
    c = connection.cursor()
    print("""In order to create a new task, we will need a name for the task and an integer
            ranging from 1 to 10 that rates its importance to you. I'll be checking to ensure
            your input is formatted correctly, so don't worry! :)""")
    time.sleep(1.0)
    task = raw_input("What would you like to add to your list?\t")
    time.sleep(0.5)
    rating = raw_input("Rate this tasks importance from 1 to 10!\t")
    sql_command = "INSERT INTO tasks VALUES "
    values = "('" + task.lower() + "', " + rating + ")"
    final_command = sql_command + values
    time.sleep(0.5)
    double_check = raw_input("Just to be safe, is this what you'd like to add?: Task is '" + task + "' and rating is " + rating + "\t")
    if double_check.lower() == "yes":
        c.execute(final_command) # Adds the desired task and rating into the table.
        connection.commit()
        connection.close()
        if (raw_input("Want to add another task?").lower() == "yes"):
            creator()
        else:
            choice_maker()
    else:
        print("That's okay, let's start over! :)")
        creator()

def complete(): #This method will complete a task and add that task to list of completed tasks
    connection = sqlite3.connect(sql_file)
    connection.text_factory = str
    c = connection.cursor()
    print("Good job! Being productive is great!")
    reprint = raw_input("Should I re-print the to-do list?\t")
    if reprint.lower() == "yes":
        c.execute('SELECT * FROM tasks')
        realList = c.fetchall()
        dicto = dict(realList)
        for key,val in dicto.items():
            print key, ":", val
    time.sleep(1.5)
    bool = True
    while (bool == True):
        completedTask = raw_input("Enter the name of task would you like to complete?\t")
        print (completedTask)
        c.execute("DELETE FROM tasks WHERE task=?", (completedTask,))
        connection.commit()
        bool = False
        repeat = raw_input("Want to complete another task?\t")
        if repeat.lower() == "yes":
            bool = True
        else:
            connection.close()
            choice_maker()

def list():
    connection = sqlite3.connect(sql_file)
    connection.text_factory = str
    c = connection.cursor()
    c.execute('SELECT * FROM tasks')
    realList = c.fetchall()
    dicto = dict(realList)
    for key,val in dicto.items():
        print key, ":", val
    if (raw_input("Would you like to do something else?").lower() == "yes"):
        choice_maker()
    else:
        connection.close()

def sort():
    connection = sqlite3.connect(sql_file)
    connection.text_factory = str
    c = connection.cursor()
    print("Would you like to sort by task name or importance of task?")
    time.sleep(0.5)
    importanceOrTask = raw_input("Enter A for task name and B for importance\t")
    if (importanceOrTask.lower() == "a"):
        for row in c.execute("SELECT * FROM tasks ORDER BY task ASC"):
            print row
        if (raw_input("Would you like to do something else?").lower() == "yes"):
            choice_maker()
        else:
            sys.exit()
            connection.close()
        connection.close()
    elif (importanceOrTask.lower() == "b"):
        for row in c.execute("SELECT * FROM tasks ORDER BY importance DESC"):
            print row
        if (raw_input("Would you like to do something else?").lower() == "yes"):
            choice_maker()
        else:
            sys.exit()
            connection.close()
            
run()
