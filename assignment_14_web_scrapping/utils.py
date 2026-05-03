"""This module contains utility functions."""
import re
from datetime import datetime, timedelta

import dateparser


def get_date_from_string(date_string: str) -> datetime:
    """
    Returns a datetime object for the given date string

    Args:
        date_string (str): the date string to parse
    Returns:
        datetime: datetime object for the given date string
    """
    clean_str = date_string.lower().replace("updated", "").strip()
    date = re.sub(r'\b(\d+)m\b', r'\1 minutes', clean_str)
    return dateparser.parse(date, settings={
        "PREFER_DATES_FROM": "past",
        "RELATIVE_BASE": datetime.now(),
        "PARSERS": ["relative-time", "absolute-time"]
    })


def normalize_date(news_date: datetime) -> str:
    """
    Returns a string representing the given news date

    Args:
        news_date (datetime): the date to normalize
    Returns:
        str: string representing of the given news date
    """
    return news_date.strftime("%d %B %Y %H:%M")


def is_in_range(news_date: datetime, days: int) -> bool:
    """
    Checks if the given news date is an in range

    Args:
        news_date (datetime): the date to check
        days (int): the number of days to check
    Returns:
        bool: True if the given news date in range; otherwise False
    """
    diff_date = datetime.now() - timedelta(days=days)
    return news_date >= diff_date
