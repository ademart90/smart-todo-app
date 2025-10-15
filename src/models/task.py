from datetime import datetime

class Task:
    def __init__(self, description, tags=None, priority=None, due=None, assigned=None, completed=False):
        self.description = description
        self.tags = tags or []
        self.priority = priority
        self.due = due  # datetime or None
        self.assigned = assigned
        self.completed = completed

    def to_dict(self):
        return {
            "description": self.description,
            "tags": self.tags,
            "priority": self.priority,
            "due": self.due.strftime("%Y-%m-%d") if isinstance(self.due, datetime) else None,
            "assigned": self.assigned,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
         due = data.get("due")

        # ✅ Only parse if it's a string
         if isinstance(due, str):
            try:
                due = datetime.strptime(due, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    due = datetime.strptime(due, "%Y-%m-%d")
                except ValueError:
                    due = None


         return Task(
            description=data.get("description"),
            tags=data.get("tags", []),
            priority=data.get("priority"),
            due=due,
            assigned=data.get("assigned"),
            completed=data.get("completed", False)
        )

    def __repr__(self):
        return f"<Task {self.description} | Priority: {self.priority} | Due: {self.due} | Completed: {self.completed}>"

