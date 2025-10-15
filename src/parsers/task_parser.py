import re
from datetime import datetime

def parse_task(task_str):
    tags = re.findall(r"@(\w+)", task_str)
    priority_match = re.search(r"#(\w+)", task_str)
    priority = priority_match.group(1) if priority_match else None
    due_match = re.search(r"due:(\d{4}-\d{2}-\d{2})", task_str)
    due = datetime.strptime(due_match.group(1), "%Y-%m-%d") if due_match else None
    assigned_match = re.search(r"assigned:(\S+)", task_str)
    assigned = assigned_match.group(1) if assigned_match else None
    description = re.sub(r"@(\w+)|#(\w+)|due:\d{4}-\d{2}-\d{2}|assigned:\S+", "", task_str).strip()
    
    return {
        "description": description,
        "tags": tags,
        "priority": priority,
        "due": due,
        "assigned": assigned
    }