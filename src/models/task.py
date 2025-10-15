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
        """Convert Task object to dictionary to save to json)."""
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
        """Create Task object from dictionary to load from JSON)."""
        return Task( 
            description=data["description"],
            completed=data["completed"],
        )

    def __repr__(self):
        return f"<Task {self.description} | Priority: {self.priority} | Due: {self.due} | Completed: {self.completed}>"

