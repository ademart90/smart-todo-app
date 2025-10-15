import re

def validate_email(email):
    if not email:
        return True
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def validate_priority(priority):
    return priority in ["low", "medium", "high", None]

def validate_task(task_dict):
    if not validate_email(task_dict.get("assigned")):
        return False, "Invalid email"
    if not validate_priority(task_dict.get("priority")):
        return False, "Invalid priority"
    return True, "Valid task"
