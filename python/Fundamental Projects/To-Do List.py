


ToDoWorks=[]

while True:
    print("1.Enter your task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        Task=input("Enter your Task: ")
        ToDoWorks.append(Task)
        print("Your Task has been added Successfully")
    elif choice==2:
        if ToDoWorks is None:
            print("The To do list is empty!")
        else:
            for task in ToDoWorks:
                print(task)
    elif choice==3:
        for taks in ToDoWorks:
            print(taks)
        task=input("Choose which task you want to remove from this list: ")
        if task in ToDoWorks:
            ToDoWorks.remove(task)
        else:
            print("Task does not exist")
    elif choice==4:
        print("Thanks for using our services")
        print("Have a nice day!")
        break
    else:
        print("Please enter a valid choice")

































