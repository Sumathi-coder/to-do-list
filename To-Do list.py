def To_DO_list():
 tasks=[]
 while True:
    print("1. Add task")
    print("2. Remove task")
    print("3.Show task")
    print("4. quit")

    choice=int(input("enter your choice: "))
                 
    if(choice=="1"):
        task=input("enter task")
        tasks.append(task)
    elif(choice=="2"):
        task=input("enter the task to be remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("task not found")
    elif(choice=="3"):
        print("tasks: ")
        for task in tasks:
            print("-"+task)
    elif(choice=="4"):
        break
    else:
        print("INVALID CHOICE")
To_DO_list()
        
                 