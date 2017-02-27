# This is a to-do application intended to be used on the command line.
# This first iteration is merely a self-containing to-do program.
# Once the program ends, all information is lost.

import sys


def run():
    print("Hello there! What would you like to do?")
    print("Enter the corresponding code for what you'd like to do!")
    print("list: Entering 'list' will print out the contents of the to-do list!")
    print("add: Entering 'add' will allow you to enter another task.")
    print("finish: Entering 'finish' will complete one of the items.")
    print("exit: this will close the program")

    desire = raw_input("So what do you want to do?   ")

    if desire == "list":
        list()
    elif desire == "add":
        add()
    elif desire == "finish":
        finish()
    elif desire == "exit":
        exit()

def list():
    print("placeholder")
    run()

def add():
    print ("placeholder")
    run()

def finish():
    print ("placeholder")
    run()


run()
