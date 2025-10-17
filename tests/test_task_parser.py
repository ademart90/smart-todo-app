import pytest
from datetime import datetime
from src.parsers.task_parser import parse_task


def test_parse_task_full_input():
    task_str = 'Complete project @school #high due:2025-10-20 assigned:alice@example.com'
    result = parse_task(task_str)

    assert result["description"] == "Complete project"
    assert result["tags"] == ["school"]
    assert result["priority"] == "high"
    assert result["due"] == datetime(2025, 10, 20)
    assert result["assigned"] == "alice@example.com"


def test_parse_task_missing_due_and_assigned():
    task_str = 'Buy groceries @home #medium'
    result = parse_task(task_str)

    assert result["description"] == "Buy groceries"
    assert result["tags"] == ["home"]
    assert result["priority"] == "medium"
    assert result["due"] is None
    assert result["assigned"] is None


def test_parse_task_no_priority_or_tags():
    task_str = 'Call plumber due:2025-11-01 assigned:bob@example.com'
    result = parse_task(task_str)

    assert result["description"] == "Call plumber"
    assert result["tags"] == []
    assert result["priority"] is None
    assert result["due"] == datetime(2025, 11, 1)
    assert result["assigned"] == "bob@example.com"


def test_parse_task_extra_spaces():
    task_str = '   Finish report   @work   #urgent   due:2025-12-31   assigned:carol@example.com   '
    result = parse_task(task_str)

    assert result["description"] == "Finish report"
    assert result["tags"] == ["work"]
    assert result["priority"] == "urgent"
    assert result["due"] == datetime(2025, 12, 31)
    assert result["assigned"] == "carol@example.com"


def test_parse_task_no_metadata():
    task_str = "Read book"
    result = parse_task(task_str)

    assert result["description"] == "Read book"
    assert result["tags"] == []
    assert result["priority"] is None
    assert result["due"] is None
    assert result["assigned"] is None
