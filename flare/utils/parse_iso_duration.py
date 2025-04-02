import re


def parse_iso_duration(iso_duration: str) -> int:
    """
    Parse an ISO 8601 duration string and return the total number of seconds it
    """
    regex = r"P(\d+D)?T(\d+H)?(\d+M)?(\d+S)?"
    match = re.match(regex, iso_duration)
    if not match:
        raise ValueError("Invalid ISO 8601 duration format")
    days = int(match.group(1)[:-1]) if match.group(1) else 0
    hours = int(match.group(2)[:-1]) if match.group(2) else 0
    minutes = int(match.group(3)[:-1]) if match.group(3) else 0
    seconds = int(match.group(4)[:-1]) if match.group(4) else 0
    total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
    return total_seconds
