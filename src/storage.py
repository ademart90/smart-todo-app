
import json
from datetime import datetime
from models.task import Task

def save_tasks(todo_list, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump([t.__dict__ for t in todo_list.tasks], f, default=str, indent=4)


def load_tasks(todo_list, filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            
            #Clear existing tasks before loading new ones
            todo_list.tasks = []
            for t in data:
                todo_list.tasks.append(Task.from_dict(t))
    except FileNotFoundError:
        pass