## Simple To-Do List (Console Version)

VERSION = "0.1"
import time

tasks = ["Do homework", "Buy food"]

def addTask():
    print("Selected add task option!")
    time.sleep(1)
    count = input("How many tasks would you like to add to the To-Do List: ")
    try:
        count = int(count)
        
        for i in range(count):
            task = input("Input task to add to the To-Do List: ")
            tasks.append(task)
            
    except ValueError:
        print("Invalid count.")
    else:
        time.sleep(1)
        print("Successfully added task(s)!")

def viewTasks():
    print("Selected view tasks option!")
    time.sleep(1)
    print("Fetching all tasks...")
    time.sleep(1)
    print("Successfuly found tasks!")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def removeTask():
    print("Selected remove task option!")
    time.sleep(1)

    task_number = input(f"Input task number to remove: ")
    try:
        task_num = int(task_number)
        task_index = task_num - 1

        n = len(tasks)

        if task_index>= -n and task_index<n:
                    
            del tasks[task_index]

        else:
            print("Task number doesn't exist. Perhaps a typo?")

    except ValueError:
        print("Invalid count.")
    else:
        time.sleep(1)
        print("Successfully removed task(s)!")

def Main():
    print(f"----Welcome to my Simple To-Do List // Version {VERSION}----")
    while True:
        time.sleep(1)
        print("\n---OPTIONS---\n"
            "1. Add task\n" 
            "2. View tasks\n"
            "3. Remove task\n"
             "4. Exit"
        )
        chosen = input("Choose an option: ")
        if chosen == "1":
            addTask()
        elif chosen == "2":
            viewTasks()
        elif chosen == "3":
            removeTask()
        elif chosen == "4":
            print("Exitting program.")
            break
        
if VERSION == "0.1":
    Main()
else:
    print("Version error! Outdated content.")