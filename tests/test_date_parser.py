import pytest
from src.parsers.date_parser import DateParser


@pytest.fixture
def parser_instance():
    return DateParser()


def test_standard_iso_date(parser_instance):
    text = "The deadline is 2025-10-20."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-20"]


def test_slash_format_date(parser_instance):
    text = "Meeting scheduled for 14/10/2025."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-14"]


def test_textual_month_format(parser_instance):
    text = "Project ends on Oct 17th, 2025."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-17"]


def test_multiple_dates_sorted_and_unique(parser_instance):
    text = "Start: 2025-10-14, Review: 2025-10-14, End: 2025-12-05."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-14", "2025-12-05"]  # no duplicates, sorted


def test_ignores_invalid_dates(parser_instance):
    text = "Invalid date: 32/13/2025 and gibberish 2025-99-99."
    result = parser_instance.extract_and_normalize(text)
    assert result == []  # should safely skip invalid ones


def test_mixed_formats(parser_instance):
    text = "Kickoff 14/10/2025, next phase Oct 17th, 2025, final 2025-12-05."
    result = parser_instance.extract_and_normalize(text)
    assert result == ["2025-10-14", "2025-10-17", "2025-12-05"]


def test_no_date_found(parser_instance):
    text = "There is no valid date here."
    result = parser_instance.extract_and_normalize(text)
    assert result == []
