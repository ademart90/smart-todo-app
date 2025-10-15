
import json
from datetime import datetime
from models.task import Task

def save_tasks(todo_list, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump([t.__dict__ for t in todo_list.tasks], f, default=str)


def load_tasks(todo_list):
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            for t in data:
                if "due" in t and t["due"]:
                    try:
                        # Try full datetime first
                        t["due"] = datetime.strptime(t["due"], "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        # Fallback to date-only
                        t["due"] = datetime.strptime(t["due"], "%Y-%m-%d")
                todo_list.tasks.append(Task.from_dict(t))
    except FileNotFoundError:
        pass
