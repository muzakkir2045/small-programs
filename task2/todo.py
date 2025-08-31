

try:
    with open("todo.txt", "r") as f:
        tasks = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    tasks = []

def add_task():
    tasks.append(input_task := input("Enter a task: ").capitalize())
    print("Task added successfully!")
    return tasks

def view_task():
    if tasks == []:
        print("There are no tasks to show!")
    else:
        print("\n== Tasks == : ")
        for key,value in enumerate(tasks,start=1):
            print(f"{key}.{value}") 

def rmv_task():
    if tasks == []:
        print("There are no tasks to remove!")
    else:
        view_task()
        try:
            opt = int(input("Enter the task no to remove: "))
            del tasks[opt-1]
            print("Task removed successfully!")
            return tasks
        except ValueError:
            print("Please enter a valid number")

def save_tsk():
    with open("todo.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved to file")

options = [add_task,view_task,rmv_task,save_tsk]

while True:
    print("\n== Options ==")
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Save task")
    print("5. Exit\n")
    try:
        opt = int(input("Enter the option no. from above: "))
        if 0 <= opt < len(options)+1:
            options[opt-1]()  # Call the function using ()
        elif opt == 5:
            save_tsk()
            print("Exiting...")
            break
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter valid option")

