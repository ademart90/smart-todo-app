import pytest
from datetime import datetime, timedelta
from src.parsers.date_parser import DateParser  # adjust import path if needed

@pytest.fixture
def parser_instance():
    return DateParser()


def test_parse_standard_date(parser_instance):
    text = "The deadline is 2025-12-05."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-12-05"]


def test_parse_slash_format(parser_instance):
    text = "Meeting on 14/10/2025."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-14"]


def test_parse_month_name_format(parser_instance):
    text = "Project ends on Oct 17th, 2025."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-17"]


def test_parse_today(parser_instance):
    today = datetime.today().strftime("%Y-%m-%d")
    result = parser_instance.extract_and_normalize("today")
    assert result == [today]


def test_parse_tomorrow(parser_instance):
    tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    result = parser_instance.extract_and_normalize("tomorrow")
    assert result == [tomorrow]


def test_parse_yesterday(parser_instance):
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    result = parser_instance.extract_and_normalize("yesterday")
    assert result == [yesterday]


def test_parse_next_week(parser_instance):
    next_week = (datetime.today() + timedelta(weeks=1)).strftime("%Y-%m-%d")
    result = parser_instance.extract_and_normalize("next week")
    assert result == [next_week]


def test_parse_next_month(parser_instance):
    next_month = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d")
    result = parser_instance.extract_and_normalize("next month")
    assert result == [next_month]


def test_parse_multiple_dates(parser_instance):
    text = "Start on 14/10/2025 and end by 2025-12-05."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-14", "2025-12-05"]


def test_parse_mixed_text(parser_instance):
    text = "The meeting is next week, and report due 2025-12-05."
    result = parser_instance.extract_and_normalize(text)
    assert any(date in result for date in [
        (datetime.today() + timedelta(weeks=1)).strftime("%Y-%m-%d"),
        "2025-12-05"
    ])


def test_parse_invalid_text(parser_instance):
    text = "This text has no date."
    result = parser_instance.extract_and_normalize(text)
    assert result == []
