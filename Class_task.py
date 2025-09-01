# @title 13. Email Slicer(Extract Username from Email)

"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""
while True:
    mail = input("Please input your email: ")
    if mail.endswith("@gmail.com"):
        print("Verified")
        break
    else:
        print("invalid email. try again")

entry = mail.split("@")
print(entry[0])
print(entry[1])








# @title 2. To-Do List Application

"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""

my_tasks = []

def add_task(task):
    my_tasks.append(task)
    print(f"{task} has been successfully added to your to-do-list.")

def remove_task(task):
    if task in my_tasks:
        my_tasks.remove(task)
        print(f"{task} has been successfully removed from your to-do-list.")
    else:
        print(f"{task} is not on your to-do-list.")

def view_tasks(task):
    if task in my_tasks:
        print("Your tasks are:")
        for task, my_tasks in enumerate(my_tasks, 1):
            print(f"{task}. {my_tasks}")
    else:
        print("There is nothing to display.")


