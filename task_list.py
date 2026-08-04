def todo_list():
    """
    Store tasks entered by the user.

    Returns:
        None
    """

    tasks = []

    while True:
        print("[1]. Add Task\n[2]. View Task List\n[3]. Edit Task\n[4]. Exit")

        enter = int(input("Which One, You Like To Do :- "))
        if enter == 1:
            task_name = input("Enter Task Name :-")
            tasks.append(task_name)
            print()
        elif enter == 2:
            for i in tasks:
                print(i)
            print(tasks)
            print()
        elif enter == 3:
            for i in tasks:
                print(i)
            old_task = input("Which task would you like to edit :-")
            new_task = input("Enter New Task :-")
            tasks.remove(old_task)
            tasks.append(new_task)
            print()
        elif enter == 4:
            print()
            break

        else:
            print("Enter Proper Input")


todo_list()
