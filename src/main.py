from models.todo_list import TodoList

def main():
    todo = TodoList()

    while True:
        print("\n SMART TODO APP")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete/Incomplete")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)

        elif choice == "2":
            todo.list_tasks()

        elif choice == "3":
            task_id = input("Enter task ID: ")
            new_desc = input("Enter new description: ")
            todo.update_task(task_id, new_desc)

        elif choice == "4":
            task_id = input("Enter task ID: ")
            todo.delete_task(task_id)

        elif choice == "5":
            task_id = input("Enter task ID: ")
            todo.toggle_complete(task_id)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

    
