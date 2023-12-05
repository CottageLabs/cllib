import re

# ~~Date:Regex~~
BIG_END_DATE = r'^\d{4}-\d{2}-\d{2}$'
BIG_END_DATE_COMPILED = re.compile(BIG_END_DATE)

HTTP_URL = (
    r'^(?:https?)://'  # Scheme: http(s) or ftp
    r'(?:[\w-]+\.)*[\w-]+'  # Domain name (optional subdomains)
    r'(?:\.[a-z]{2,})'  # Top-level domain (e.g., .com, .org)
    r'(?:\/[^\/\s]*)*'  # Path (optional)
    r'(?:\?[^\/\s]*)?'  # Query string (optional)
    r'(?:#[^\/\s]*)?$'  # Fragment (optional)
)

HTTP_URL_COMPILED = re.compile(HTTP_URL, re.IGNORECASE)


def group_match(pattern, string, name, *args, **kwargs):
    match = re.match(pattern, string, *args, **kwargs)
    if match is None:
        return None
    return match.group(name)
