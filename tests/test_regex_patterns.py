import pytest
from src.parsers.regex_patterns import (
    search_by_keyword,
    filter_by_tag,
    filter_by_priority,
    filter_by_date,
)

@pytest.fixture
def sample_tasks():
    return [
        {"description": "Complete project report @work #high due:2025-10-20"},
        {"description": "Buy groceries @home #medium due:2025-10-15"},
        {"description": "Call the doctor @personal #low due:2025-10-12"},
        {"description": "Submit assignment @school #high due:2025-10-22"},
    ]

def test_search_by_keyword(sample_tasks):
    result = search_by_keyword(sample_tasks, "project")
    assert len(result) == 1
    assert "project" in result[0]["description"].lower()

def test_filter_by_tag(sample_tasks):
    result = filter_by_tag(sample_tasks, "school")
    assert len(result) == 1
    assert "@school" in result[0]["description"]

def test_filter_by_priority(sample_tasks):
    result = filter_by_priority(sample_tasks, "high")
    assert len(result) == 2  # 2 tasks with #high
    for task in result:
        assert "#high" in task["description"]

def test_filter_by_date(sample_tasks):
    result = filter_by_date(sample_tasks, "2025-10-20")
    assert len(result) == 1
    assert "2025-10-20" in result[0]["description"]
