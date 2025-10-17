from models.task import Task
import json
from pathlib import Path

class TodoList:
    def __init__(self, storage_file="tasks.json"):
        self.storage_file = Path(storage_file)
        self.tasks = []
        self.load_tasks()

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.save_tasks()

    def save_tasks(self):
        """Save all tasks as dictionaries to JSON"""
        with open(self.storage_file, "w") as file:
            json.dump([t.to_dict() for t in self.tasks], file, indent=4)

    def load_tasks(self):
        """Load tasks safely from JSON"""
        if self.storage_file.exists():
            with open(self.storage_file, "r") as file:
                try:
                    data = json.load(file)
                    # Convert dictionaries back into Task objects
                    self.tasks = [Task.from_dict(t) for t in data if isinstance(t, dict)]
                except json.JSONDecodeError:
                    self.tasks = []
    
    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

    def search_by_keyword(self, keyword):
        return [t for t in self.tasks if keyword.lower() in t.description.lower()]

    def search_by_priority(self, priority):
        return [t for t in self.tasks if t.priority == priority]

    def filter_by_tag(self, tag):
        return [t for t in self.tasks if tag in t.tags]

    
    def filter_by_date(self, due):
        return [task for task in self.tasks if task.due == due ]


    def mark_complete(self, index):
        self.tasks[index].completed = True

    def mark_incomplete(self, index):
        self.tasks[index].completed = False

    def update_task(self, index, **kwargs):
        task = self.tasks[index]
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)

    def delete_task(self, index):
        self.tasks.pop(index)
