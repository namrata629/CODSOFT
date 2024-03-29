tasks = []

def addtask():
    task=input("please enter a task: ")
    tasks.append(task)
    print(f"task '(task)' added to the list:")
def listtask():
    if not tasks:
        print("there are no task currently: ")
    else:
        print("current task: ")
        for index, task in enumerate(tasks):
            print(f"task #{index}. {tasks}:")
def deletetask():
    listtask()
    try:
        tasktodelete =int(input("enter the value u want to delete :"))
        if tasktodelete >=0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"task {tasktodelete} has been removed")
        else:
            print(f"task #{tasktodelete} was not found :")
    except:
        print("invalid input: ")



if __name__=="__main__":
    print("Welcome to the to do list app :")
    while True:
        print("\n")
        print("please select one of the option: ")
        print("1. Add a new task: ")
        print("2. Delete a task: ")
        print("3. List a task; ")
        print("4. Quit ")

        choice = input("enter your choice: ")

        if(choice=="1"):
            addtask()
        elif(choice=="2"):
            deletetask()
        elif(choice=="3"):
            listtask()
        elif(choice=="4"):
            break
        else:
            print("invalid input please try again ")