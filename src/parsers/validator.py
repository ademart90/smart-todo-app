import re

EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

def is_valid_email(email):
    """Return True if email is valid."""
    if not email:
        return False
    return EMAIL_REGEX.match(email) is not None
