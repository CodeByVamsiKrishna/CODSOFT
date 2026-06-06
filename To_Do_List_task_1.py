available_options = [
    "View Task",
    "Add Task",
    "Delete Task",
    "Task Status & Update",
    "Search Task",
    "Exit"
]

available_task = [
    "Wake up at morning",
    "Learn coding",
    "Practice everything learned",
    "Don't waste the time"
]

task_status = [
    "pending",
    "pending",
    "pending",
    "pending"
]

while True:

    count = 0
    for task in available_options:
        count +=1
        print(count, task)

    task_number = int(input("Enter the task number to perform task : "))

    if task_number == 1:
        for task in available_task:
            print(task)

    elif task_number == 2:
        new_task = input("Enter the new task to add : ")
        available_task.append(new_task)
        task_status.append("pending")
        print("New task added succesfully ")

    elif task_number == 3:
        count=0
        for task in available_task:
            count+=1
            print(count,task)

        to_delete_task = int(input("Enter task number to delete : "))
        to_delete_task -=1
        available_task.remove(available_task[to_delete_task])

        print("Removed succesfully")

        count= 0
        for task in available_task:
            count+=1
            print(count,task)

    elif task_number == 4:
        count=count2=0

        for task in available_task:
            print(count+1,task," - ",task_status[count])
            count+=1

        completed_task = int(input("Enter task number to mark as completed : "))
        completed_task-=1

        task_status[completed_task] = "completed"

        print("Succesfully marked as completed")

        for task in available_task:
            print(count2+1,available_task[count2],"-",task_status[count2])
            count2+=1

    elif task_number==5:
        count = 0

        find_task = input("Enter task name to search : ")

        for task in available_task:
            if task.lower() == find_task.lower():
                print("Task found")
                count+=1
                break

        if count==0:
            print("Task not found")

    elif task_number == 6:
        print("Thank you for using Task Manager. Goodbye!")
        break
