from .regex_patterns import TAG_PATTERN, PRIORITY_PATTERN, DATE_PATTERN, EMAIL_PATTERN
import re

def parse_task_input(text):
    """Extract components from natural language task input."""
    tags = TAG_PATTERN.findall(text)
    priority_match = PRIORITY_PATTERN.search(text)
    date_match = DATE_PATTERN.search(text)
    email_match = EMAIL_PATTERN.search(text)

    priority = priority_match.group(1).lower() if priority_match else None
    due_date = date_match.group(1) if date_match else None
    assigned_to = email_match.group(1) if email_match else None

    # Extract all recognized patterns from the description
    cleaned_text = re.sub(r'(@\w+|#\w+|due:[\w\-\s]+|assigned:[\w\.-]+@[\w\.-]+\.\w+)', '', text).strip()

    return {
        "description": cleaned_text,
        "tags": tags,
        "priority": priority,
        "due_date": due_date,
        "assigned_to": assigned_to
    }
