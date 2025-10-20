import re
from datetime import datetime

def parse_task(task_str):
    tags = re.findall(r"(?<![\w.])@(\w+)\b", task_str)
    priority_match = re.search(r"#(\w+)", task_str)
    priority = priority_match.group(1) if priority_match else None
    due_match = due_match = re.search(r"due:([\w\-]+)", task_str)
    due = due_match.group(1) if due_match else None
    assigned_match = re.search(r"assigned:(\S+)", task_str)
    assigned = assigned_match.group(1) if assigned_match else None
    description = re.sub(r"@(\w+)|#(\w+)|due:([\w\-]+)|assigned:\S+", "", task_str).strip()
    
    return {
        "description": description,
        "tags": tags,
        "priority": priority,
        "due": due,
        "assigned": assigned
    }
