import re

#Regex patterns for the different components
TAG_PATTERN = re.compile(r'@(\w+)')
PRIORITY_PATTERN = re.compile(r'#(high|medium|low)', re.IGNORECASE)
DATE_PATTERN = re.compile(r'due:(\d{4}-\d{2}-\d{2}|tomorrow|next week)', re.IGNORECASE)
EMAIL_PATTERN = re.compile(r'assigned:([\w\.-]+@[\w\.-]+\.\w+)', re.IGNORECASE)
