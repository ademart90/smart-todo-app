# src/models/todo_list.py
import json
import os
from models.task import Task

DATA_FILE = os.path.join("data", "tasks.json")

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file if it exists."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(t) for t in data]
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to JSON file."""
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w") as file:
            json.dump([t.to_dict() for t in self.tasks], file, indent=4)

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {task.description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n Your Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                self.save_tasks()
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()
        print("Task deleted successfully.")

    def toggle_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                self.save_tasks()
                print("Task completed")
                return
        print("Task not found")
