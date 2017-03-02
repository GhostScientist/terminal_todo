# This is a to-do application intended to be used on the command line.
# This first iteration is merely a self-containing to-do program.
# Once the program ends, all information is lost.

# Created by Dakota Kim.

import sys
import sqlite3
import os
import time


def run():
    print("(Hi there, if at anytime you'd like to quit this program, enter 'EXIT' into any input field)")
    time.sleep(1.0) # This program will use a lot of sleeping so the user isn't bombarded with information.
    response = raw_input("Hello! Is this your first time creating a to-do list in the terminal?\t")
    # If this is first time, will run the createDB method to create a database to store tasks.
    if response.lower() == "yes":
        createDB()
    elif response.lower() == "no":
        choice_maker()
    elif response.lower() == "create":
        creator()
    elif choice.upper() == "EXIT":
        sys.exit()

def createDB():
    pwd = os.getcwd() ## Returns the current directory. I'll add some customization to this section later.
    print("Awesome! Let's get started")
    time.sleep(0.5)
    print("Your current directory is " + pwd)
    time.sleep(0.5)
    print("Keep track of this path! Your database will be created here!")
    sql_file = pwd + "/my_todo.db"
    connection = sqlite3.connect(sql_file)
    c = connection.cursor()
    # We have connected a database file. If file doesn't already exist, this connection
    # will create it. The next step is to create a table.
    c.execute('''CREATE TABLE tasks(TEXT task, INTEGER importance)''')
    # Eventually I would like to have a way for users to sort by what is due soonest.
    # Perhaps a MM/DD/YYYY implementation. I'll do some research into that. :)

def choice_maker():
    # The manager method will allow the user to control the contents of their to-do list.
    # The user will select a number that corresponds to their desire. I will implement
    # a tracking system for the user to keep track of how many tasks they've completed
    # and which ones! I will also implement a sorting method for users to decide which
    # criteria they'd like to sort by. :)
    print("""What would you like to do?
                       1 = Add a new task
                       2 = Complete a task
                       3 = Remove a task
                       4 = List all tasks
                       5 = Sort tasks!""")
    time.sleep(1.0)
    choice = raw_input("Enter the number that corresponds to your choice!    ")
    if (choice.isdigit()):
        if choice == "1":
            print("You chose 1!")
            sys.exit()
        elif choice == "2":
            print("You chose 2!")
            sys.exit()
        elif choice == "3":
            print("You chose 3!")
            sys.exit()
        elif choice == "4":
            print("You chose 4!")
            sys.exit()
        elif choice == "5":
            print("You chose 5!")
            sys.exit()
        elif choice.upper() == "EXIT":
            sys.exit()
        else:
            print ("You didn't enter a valid choice! Select a choice ranging from 1 to 5!")
            choice_maker()
    else:
        print("You didn't enter a valid number. :( No problem! We can start all over again! :D")
        choice_maker()

def creator(): # Method used to create new tasks for the list.
    print("""In order to create a new task, we will need a name for the task and an integer
            ranging from 1 to 10 that rates its importance to you. I'll be checking to ensure
            your input is formatted correctly, so don't worry! :)""")
    time.sleep(1.0)
    task = raw_input("What would you like to add to your list?  ")
    time.sleep(0.5)
    rating = raw_input("Rate this tasks importance from 1 to 10!    ")
    sql_command = "INSERT INTO tasks VALUES "
    values = "('" + task + "', " + rating + ")"
    final_command = sql_command + values
    time.sleep(0.5)
    double_check = raw_input("Just to be safe, is this what you'd like to add?: Task is '" + task + "' and rating is " + rating)
    if double_check.lower() == "yes":
        c.execute(final_command) # Adds the desired task and rating into the table.
        c.commit()
    else:
        print("That's okay, let's start over! :)")
        creator()

#def compete(): This method will complete a task and add that task to list of completed tasks

#def remove():

#def list():

#def sort():

run()
