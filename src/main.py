from cli.interface import *

def main():
    load_tasks(todo_list)
    while True:
        print("\nOptions: add | list | search_by_keyword | search_by_priority | filter_by_tag | filter_by_due | mark_complete | mark_incomplete | update | delete | exit")
        choice = input("Enter choice: ").strip().lower()

        if choice == "add":
            task_str = input("Enter task: ")
            add_task_interface(task_str)
        elif choice == "list":
            list_interface()
        elif choice == "search_by_keyword":
            keyword = input("Enter keyword: ")
            search_interface(keyword)
        elif choice == "search_by_priority":
            search_priority_interface()
        elif choice == "filter_by_tag":
            filter_tag_interface()
        elif choice == "filter_by_due":
            filter_due_interface()
        elif choice == "mark_complete":
            mark_interface()
        elif choice == "mark_incomplete":
            unmark_interface()
        elif choice == "update":
            update_interface()
        elif choice == "delete":
            delete_interface()
        elif choice == "exit":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()