from parsers.task_parser import parse_task
from parsers.validator import validate_task
from models.task import Task
from models.todo_list import TodoList
from storage import save_tasks, load_tasks

todo_list = TodoList()


def add_task_interface(task_str):
    task_data = parse_task(task_str)
    valid, msg = validate_task(task_data)
    if not valid:
        print("Error:", msg)
        return
    task = Task(**task_data)  # Create Task object
    todo_list.add_task(task)
    print(f"✓ Task added: {task.description}")
    
    details = []
    if getattr(task, "tags", None):
        details.append(f"Tags: {', '.join(task.tags)}")
    if getattr(task, "priority", None):
        details.append(f"Priority: {task.priority}")
    if getattr(task, "due", None):
        details.append(f"Due: {task.due}")

    if details:
        print("  " + " | ".join(details))

def list_interface():
    todo_list.list_tasks()

def search_interface(keyword):
    results = todo_list.search_by_keyword(keyword)
    if not results:
        print("No tasks found.")
        return
    for t in results:
        print(t)

def search_priority_interface():
    priority = input("Enter priority (low, medium, high): ").lower()
    results = todo_list.search_by_priority(priority)
    if not results:
        print(f"No tasks with priority {priority}")
        return
    for t in results:
        print(t)

def filter_tag_interface():
    tag = input("Enter tag to filter: ")
    results = todo_list.filter_by_tag(tag)
    if not results:
        print(f"No tasks with tag {tag}")
        return
    for t in results:
        print(t)

def filter_due_interface():
    due = input("Enter due date (YYYY-MM-DD): ")
    results = todo_list.filter_by_due_date(due)
    if not results:
        print(f"No tasks due on {due}")
        return
    for t in results:
        print(t)

def mark_interface():
    index = int(input("Enter task index to mark complete: "))
    todo_list.mark_complete(index)
    save_tasks(todo_list)
    print("Task marked complete!")

def unmark_interface():
    index = int(input("Enter task index to mark incomplete: "))
    todo_list.mark_incomplete(index)
    save_tasks(todo_list)
    print("Task marked incomplete!")

def update_interface():
    index = int(input("Enter task index to update: "))
    field = input("Enter field to update (description, priority, assigned): ")
    value = input(f"Enter new value for {field}: ")
    todo_list.update_task(index, **{field: value})
    save_tasks(todo_list)
    print("Task updated!")

def delete_interface():
    index = int(input("Enter task index to delete: "))
    todo_list.delete_task(index)
    save_tasks(todo_list)
    print("Task deleted!")
