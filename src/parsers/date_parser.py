import re
from datetime import datetime, timedelta
from dateutil import parser

class DateParser:
    def __init__(self):
        # Matches common date formats
        self.date_patterns = [
           r"\b\d{4}-\d{2}-\d{2}\b",  # 2025-12-05
           r"\b\d{1,2}/\d{1,2}/\d{4}\b",  # 14/10/2025
           r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}(?:st|nd|rd|th)?[,]?\s*\d{4}\b"  # Oct 17th, 2025
]

    def clean_text(self, text):
        """Remove ordinal suffixes (st, nd, rd, th) from dates."""
        return re.sub(r'(\d+)(st|nd|rd|th)', r'\1', text)

    def extract_and_normalize(self, text):
        text = self.clean_text(text.strip().lower())
        dates = []
        today = datetime.today()

        # Handles natural language keywords
        if "today" in text:
            return [today.strftime("%Y-%m-%d")]
        elif "tomorrow" in text:
            return [(today + timedelta(days=1)).strftime("%Y-%m-%d")]
        elif "yesterday" in text:
            return [(today - timedelta(days=1)).strftime("%Y-%m-%d")]
        elif "next week" in text:
            return [(today + timedelta(weeks=1)).strftime("%Y-%m-%d")]
        elif "next month" in text:
            return [(today + timedelta(days=30)).strftime("%Y-%m-%d")]

        # Try regex-based date extraction
        for pattern in self.date_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                try:
                    parsed_date = parser.parse(match, fuzzy=True)
                    dates.append(parsed_date.strftime("%Y-%m-%d"))
                except Exception:
                    continue

        # Try general fuzzy parse if no regex match
        if not dates:
            try:
                parsed_date = parser.parse(text, fuzzy=True)
                dates.append(parsed_date.strftime("%Y-%m-%d"))
            except Exception:
                pass

        return sorted(set(dates))  # remove duplicates and sort


if __name__ == "__main__":
    parser_instance = DateParser()
    examples = [
        "today",
        "tomorrow",
        "next week",
        "next month",
        "14/10/2025",
        "Oct 17th, 2025",
        "The project starts next week and ends 2025-12-05"
    ]

    for text in examples:
        print(f"Input: {text}")
        print("Extracted:", parser_instance.extract_and_normalize(text))
        print("-" * 40)

