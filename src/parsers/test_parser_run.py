from src.parsers.task_parser import parse_task_input
from src.parsers.validator import is_valid_email

text = "Buy groceries @shopping #high due:2025-10-20 assigned:alice@example.com"
parsed = parse_task_input(text)
print(parsed)
print("Valid Email:", is_valid_email(parsed["assigned_to"]))
