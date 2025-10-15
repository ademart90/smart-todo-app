from src.parsers.regex_patterns import (
    search_by_keyword,
    filter_by_tag,
    filter_by_priority,
    filter_by_date,
)

# Sample tasks
tasks = [
    {"description": "Buy groceries @shopping #high due:2025-10-20"},
    {"description": "Submit report @work #medium due:2025-10-15"},
    {"description": "Plan birthday party @personal #low due:2025-11-01"},
    {"description": "Pay electricity bill @bills #high due:2025-10-25"},
]

print("Keyword Search (e.g., 'report'):")
print(search_by_keyword(tasks, "report"))
print()

print("Filter by Tag (@shopping):")
print(filter_by_tag(tasks, "shopping"))
print()

print("Filter by Priority (#high):")
print(filter_by_priority(tasks, "high"))
print()

print("Filter by Date (2025-10):")
print(filter_by_date(tasks, "2025-10"))
print()
