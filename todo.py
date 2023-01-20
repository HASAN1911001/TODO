import datetime
import uuid

class Task:
    def __init__(self, name, created_time,id, updated_time=None, complete_time=None, task_done=False):
        self.name = name
        self.created_time = created_time
        self.updated_time = updated_time
        self.completed_time = complete_time
        self.task_done = task_done
        self.id = id

    
    def update_task(self):
        name = input("Enter New Task Name: ")

        self.name = name
        self.updated_time = datetime.datetime.now()

        print("\n")
        print("Task Updated Successfully")
        print("\n")

    
    def complete_task(self):
        self.task_done = True
        self.completed_time = datetime.datetime.now()

        print("\n")
        print("Task Completed Successfully")
        print("\n")


# Driver code

tasks = []

while(True):
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")
    
    choice = input("Enter Option: ")

    if(choice == '1'):
        name = input("Enter new task: ")
        task = Task(name,datetime.datetime.now(), uuid.uuid1())
        tasks.append(task)
        print("\n")
        print("Task Created Successfully")
        print("\n")

    elif(choice == '2'):
        for i, task in enumerate(tasks):

            print("\n", end='')
            print(f"Task-{i+1}")
            print(f"Task ID        : {task.id}")
            print(f"Task Name      : {task.name}")
            print(f"Created Time   : {task.created_time}")
            print(f"Updated Time   : {task.updated_time}")
            print(f"Complete Time  : {task.completed_time}")
            print(f"Task Done      : {task.task_done}")
            print("\n")
    elif(choice == '3'):
        count = 0
        for i, task in enumerate(tasks):
            if task.task_done == False:
                count += 1

                print("\n", end='')
                print(f"Task-{i+1}")
                print(f"Task ID        : {task.id}")
                print(f"Task Name      : {task.name}")
                print(f"Created Time   : {task.created_time}")
                print(f"Updated Time   : {task.updated_time}")
                print(f"Complete Time  : {task.completed_time}")
                print(f"Task Done      : {task.task_done}")
                print("\n")

        if count == 0:
            print("\n")
            print("No Incomplete Tasks")
            print("\n")

    elif(choice == '4'):
        count = 0
        for i, task in enumerate(tasks):
            if task.task_done == True:
                count += 1

                print("\n", end='')
                print(f"Task-{i+1}")
                print(f"Task ID        : {task.id}")
                print(f"Task Name      : {task.name}")
                print(f"Created Time   : {task.created_time}")
                print(f"Updated Time   : {task.updated_time}")
                print(f"Complete Time  : {task.completed_time}")
                print(f"Task Done      : {task.task_done}")
                print("\n")

        if count == 0:
            print("\n")
            print("No Completed Tasks")
            print("\n")

    
    elif(choice == '5'):
        print("\n")
        count = 0
        for task in tasks:
            if task.task_done == False:
                count += 1
        if count == 0:
            print("No task to update")
            print("\n")

        else:
            print("Select which task to update")
            for i, task in enumerate(tasks):
                if task.task_done == False:
                    print("\n", end='')
                    print(f"Task-{i+1}")
                    print(f"Task ID        : {task.id}")
                    print(f"Task Name      : {task.name}")
                    print(f"Created Time   : {task.created_time}")
                    print(f"Updated Time   : {task.updated_time}")
                    print(f"Complete Time  : {task.completed_time}")
                    print(f"Task Done      : {task.task_done}")
                    print("\n")
            
            task_number = int(input("Enter Task Number: "))
            task = tasks[task_number-1]

            task.update_task()
        



    elif(choice == '6'):

        print("\n")
        count = 0
        for task in tasks:
            if task.task_done == False:
                count += 1
        if count == 0:
            print("No task to complete")
            print("\n")

        else:
            print("Select which task to Complete")
            for i, task in enumerate(tasks):
                if task.task_done == False:
                    print("\n", end='')
                    print(f"Task-{i+1}")
                    print(f"Task ID        : {task.id}")
                    print(f"Task Name      : {task.name}")
                    print(f"Created Time   : {task.created_time}")
                    print(f"Updated Time   : {task.updated_time}")
                    print(f"Complete Time  : {task.completed_time}")
                    print(f"Task Done      : {task.task_done}")
                    print("\n")
            
            task_number = int(input("Enter Task Number: "))
            task = tasks[task_number-1]

            task.complete_task()