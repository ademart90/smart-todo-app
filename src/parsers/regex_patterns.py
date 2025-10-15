import re

def search_by_keyword(tasks, keyword):
    pattern = re.compile(keyword, re.IGNORECASE)
    return [task for task in tasks if pattern.search(task["description"])]

def filter_by_tag(tasks, tag):
    pattern = re.compile(rf"@{tag}\b", re.IGNORECASE)
    return [task for task in tasks if pattern.search(task["description"])]

def filter_by_priority(tasks, priority):
    pattern = re.compile(rf"#{priority}\b", re.IGNORECASE)
    return [task for task in tasks if pattern.search(task["description"])]

def filter_by_date(tasks, date_pattern):
    pattern = re.compile(rf"{date_pattern}")
    return [task for task in tasks if pattern.search(task["description"])]
