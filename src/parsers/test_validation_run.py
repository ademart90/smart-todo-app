from src.parsers.validator import (
    is_valid_date,
    is_valid_priority,
    is_valid_tag,
    is_valid_task_id,
)

test_samples = {
    "dates": ["2025-10-20", "2025/10/20", "20-10-2025", "tomorrow"],
    "priorities": ["#high", "#medium", "#urgent", "high"],
    "tags": ["@shopping", "@work", "@home!", "personal"],
    "task_ids": ["TASK-001", "T-2025-15", "TASK_", "12345"]
}

print("Test Validation Results:\n")

for d in test_samples["dates"]:
    print(f"Date '{d}': {is_valid_date(d)}")

for p in test_samples["priorities"]:
    print(f"Priority '{p}': {is_valid_priority(p)}")

for t in test_samples["tags"]:
    print(f"Tag '{t}': {is_valid_tag(t)}")

for i in test_samples["task_ids"]:
    print(f"Task ID '{i}': {is_valid_task_id(i)}")

