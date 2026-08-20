import json

print("===== Student Task Manager =====")

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

while True:
    print()
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "completed": False})

        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task added successfully! ✅")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\n===== Your Tasks =====")

            for number, item in enumerate(tasks, 1):
                status = "✅" if item["completed"] else "❌"
                print(number, "-", item["task"], status)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            for number, item in enumerate(tasks, 1):
                status = "✅" if item["completed"] else "❌"
                print(number, "-", item["task"], status)

            number = int(input("Enter task number to mark as completed: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True

                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)

                print("Task completed! ✅")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for number, item in enumerate(tasks, 1):
                status = "✅" if item["completed"] else "❌"
                print(number, "-", item["task"], status)

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted_task = tasks.pop(number - 1)

                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)

                print("Deleted:", deleted_task["task"])
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using Student Task Manager! 👋")
        break

    else:
        print("Invalid choice. Please choose 1-5.")