import re
from datetime import datetime

def parse_task_input(text: str) -> dict:
    """
    Parses a natural language task input and extracts components using regex.
    Example:
    "Buy groceries @shopping #high due:2025-10-20 assigned:alice@example.com"
    """

    # Extract tags (e.g., @shopping)
    tags = re.findall(r'@(\w+)', text)

    # Extract priority (e.g., #high)
    priority_match = re.search(r'#(\w+)', text)
    priority = priority_match.group(1).lower() if priority_match else None

    # Extract due date (e.g., due:2025-10-20)
    due_match = re.search(r'due:(\d{4}-\d{2}-\d{2})', text)
    due_date = None
    if due_match:
        try:
            due_date = datetime.strptime(due_match.group(1), "%Y-%m-%d").date()
        except ValueError:
            pass

    # Extract assigned email (e.g., assigned:alice@example.com)
    assigned_match = re.search(r'assigned:([\w\.-]+@[\w\.-]+)', text)
    assigned_to = assigned_match.group(1) if assigned_match else None

    # Remove extracted parts to isolate the task description
    cleaned_text = re.sub(r'(@\w+|#\w+|due:\S+|assigned:\S+)', '', text).strip()

    return {
        "description": cleaned_text,
        "tags": tags,
        "priority": priority,
        "due_date": due_date,
        "assigned_to": assigned_to
    }
