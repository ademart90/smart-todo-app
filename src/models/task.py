
import uuid
from datetime import datetime

class Task:
    def __init__(self, description: str, completed: bool = False, task_id: str = None):
        self.id = task_id or str(uuid.uuid4())  # unique ID
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        """Convert Task object to dictionary (for saving to JSON)."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        """Create Task object from dictionary (for loading from JSON)."""
        return Task(
            description=data["description"],
            completed=data["completed"],
            task_id=data["id"],
        )

    def __repr__(self):
        status = "completed" if self.completed else "not completed"
        return f"[{status}] {self.description} (ID: {self.id[:8]})"
