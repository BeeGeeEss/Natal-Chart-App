"""
Validators for Natal Chart Application  

"""

from datetime import datetime
import difflib
import pytz


def validate_date(date_str):
    """Validate and parse a date string in YYYY-MM-DD format"""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Invalid date format! Please use YYYY-MM-DD.") from exc
    return dt.year, dt.month, dt.day


def validate_time(time_str):
    """Validate and parse a time string in HH:MM (24-hour) format"""
    try:
        tm = datetime.strptime(time_str, "%H:%M")
    except ValueError as exc:
        raise ValueError("Invalid time format! Please use HH:MM (24-hour).") from exc
    return tm.hour, tm.minute


def validate_latitude(value_str):
    """Validate that the latitude is a float between -90 and 90, and includes a decimal"""
    if not value_str or not isinstance(value_str, str):
        raise ValueError("Latitude input must not be empty.")
    if '.' not in value_str:
        raise ValueError("Latitude must include a decimal (e.g. -37.813629)")
    try:
        val = float(value_str)
    except ValueError as exc:
        raise ValueError("Latitude must be a valid number with a decimal "
        "(e.g. -37.813629)") from exc
    if not -90 <= val <= 90:
        raise ValueError("Latitude must be between -90 and 90")
    return val


def validate_longitude(value_str):
    """Validate that the longitude is a float between -180 and 180, and includes a decimal"""
    if not value_str or not isinstance(value_str, str):
        raise ValueError("Longitude input must not be empty")
    if '.' not in value_str:
        raise ValueError("Longitude must include a decimal (e.g. 144.9631)")
    try:
        val = float(value_str)
    except ValueError as exc:
        raise ValueError("Longitude must be a valid number with a decimal (e.g. 144.9631)") from exc
    if not -180 <= val <= 180:
        raise ValueError("Longitude must be between -180 and 180")
    return val


def validate_timezone(tz_str):
    """Validate a timezone input, offering suggestions for close matches if invalid"""
    if tz_str in pytz.all_timezones:
        return tz_str

    matches = difflib.get_close_matches(tz_str, pytz.all_timezones, n=1, cutoff=0.6)
    if matches:
        raise ValueError(f"Did you mean: {matches[0]}?")
    else:
        raise ValueError("Timezone must match a real timezone like Australia/Melbourne.")
