import re
from datetime import datetime
from dateutil import parser

class DateParser:
    def __init__(self):
        # Matches common date formats
        self.date_patterns = [
            r"\b\d{4}-\d{2}-\d{2}\b",  # 2025-12-05
            r"\b\d{1,2}/\d{1,2}/\d{4}\b",  # 14/10/2025
            r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}(?:st|nd|rd|th)?,?\s+\d{4}\b"  # Oct 17th, 2025
        ]

    def clean_text(self, text):
        """Remove ordinal suffixes (st, nd, rd, th) from dates."""
        return re.sub(r'(\d+)(st|nd|rd|th)', r'\1', text)

    def extract_and_normalize(self, text):
        text = self.clean_text(text)
        dates = []
        for pattern in self.date_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                try:
                    parsed_date = parser.parse(match, fuzzy=True)
                    dates.append(parsed_date.strftime("%Y-%m-%d"))
                except Exception:
                    continue
        return sorted(set(dates))  # remove duplicates and sort

if __name__ == "__main__":
    parser_instance = DateParser()
    text = """
    The project started on 14/10/2025 and will end by Oct 17th, 2025.
    Another milestone is expected around 2025-12-05.
    """
    print(parser_instance.extract_and_normalize(text))
