import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))



# Date validation
def is_valid_date(date_str: str) -> bool:
    pattern = r"^\d{4}-\d{2}-\d{2}$"  # YYYY-MM-DD format
    if not re.match(pattern, date_str):
        return False
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Priority levels validation
def is_valid_priority(priority: str) -> bool:
    pattern = r"^#(high|medium|low)$"
    return re.match(pattern, priority, re.IGNORECASE) is not None


# Tag validation
def is_valid_tag(tag: str) -> bool:
    pattern = r"^@[a-zA-Z0-9_]+$"
    return re.match(pattern, tag) is not None


# Task ID validation
def is_valid_task_id(task_id: str) -> bool:
    pattern = r"^(T|TASK)-\d+$"
    return re.match(pattern, task_id, re.IGNORECASE) is not None


# Combined validator
def validate_task_fields(task: dict) -> dict:
    """
    This returns a dictionary indicating validation results for each field.
    """
    results = {}

    if "due_date" in task:
        results["due_date"] = is_valid_date(task["due_date"])

    if "priority" in task:
        results["priority"] = is_valid_priority(task["priority"])

    if "tags" in task and isinstance(task["tags"], list):
        results["tags"] = all(is_valid_tag(tag) for tag in task["tags"])

    if "task_id" in task:
        results["task_id"] = is_valid_task_id(task["task_id"])

    if "assigned_to" in task:
        results["assigned_to"] = is_valid_email(task["assigned_to"])

    return results
