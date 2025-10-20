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
        """Convert Task object to dictionary to save to JSON."""
        
        return {
            "description": self.description,
            "tags": self.tags,
            "priority": self.priority,
            "due": self.due,
            "assigned": self.assigned,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        """Create Task object from dictionary to load from JSON."""
        return Task(
            description=data["description"],
            completed=data["completed"],
            tags=data.get("tags", []),
            priority=data.get("priority"),
            due=data.get("due"),
            assigned=data.get("assigned")
        )

    def __repr__(self):
        return f"<Task {self.description} | Tags: {self.tags} | Priority: {self.priority} | Due: {self.due} | Completed: {self.completed}>"
