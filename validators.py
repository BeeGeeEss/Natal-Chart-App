"""
Validators for Natal Chart Application  

"""

from datetime import datetime
import pytz

def validate_date(date_str):
    """Function to align input with datetime library for formatting"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.year, dt.month, dt.day

def validate_time(time_str):
    """Function to align input with datetime library for formatting"""
    tm = datetime.strptime(time_str, "%H:%M")
    return tm.hour, tm.minute

def validate_latitude(value_str):
    """Function to ensure that the coordinates are formatted correctly"""
    if '.' not in value_str:
        raise ValueError("Latitude must include a decimal (e.g. -37.813629)")
    val = float(value_str)
    if not -90 <= val <= 90:
        raise ValueError("Latitude must be between -90 and 90")
    return val

def validate_longitude(value_str):
    """Function to ensure that the coordinates are formatted correctly"""
    if '.' not in value_str:
        raise ValueError("Latitude must include a decimal (e.g. -37.813629)")
    val = float(value_str)
    if not -180 <= val <= 180:
        raise ValueError("Longitude must be between -180 and 180")
    return val

def validate_timezone(tz_str):
    """Function to align input with pytz library for timezone"""
    if tz_str not in pytz.all_timezones:
        raise ValueError("Timezone must match a real timezone like Australia/Melbourne.")
    return tz_str
