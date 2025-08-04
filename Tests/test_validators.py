"""
Unit Testing for Validators for Natal Chart Application  

"""
import pytest
from validators import (
    validate_date,
    validate_time,
    validate_latitude,
    validate_longitude,
    validate_timezone,
)

#Unit Tests for Date Validation
def test_validate_date_valid():
    """
    Test case for the validate_date() function.

    This test checks if the validate_date() function correctly accepts the 
    date input.

    Example:
        ("2020-01-15") == "2020, 1, 15"
    Output: "2020-01-15" > Next question
    """
    assert validate_date("2020-01-15") == (2020, 1, 15)

def test_validate_date_invalid_format():
    """
    Test case for the validate_date() function.

    This test checks if the validate_date() function raises a ValueError
    when the input is not in the correct format for a date (back-to-front).

    Example:
        ("15-01-2020") == "ValueError"
    Output: "2020-01-15" == "Invalid date format! Please use YYYY-MM-DD."
    """
    with pytest.raises(ValueError):
        validate_date("15-01-2020")

def test_validate_date_invalid_d_m_format():
    """
    Test case for the validate_date() function.

    This test checks if the validate_date() function raises a ValueError
    when the input is not in the correct format for a date (day-before-month).

    Example:
        ("2000-30-05") == "ValueError"
    Output: "2020-01-15" == "Invalid date format! Please use YYYY-MM-DD."
    """
    with pytest.raises(ValueError):
        validate_date("2000-30-05")


#Unit Tests for Time Validation
def test_validate_time_valid():
    """
    Test case for the validate_time() function.

    This test checks if the validate_time() function correctly accepts the time 
    input.

    Example:
        ("13:45") == "13, 45"
    Output: "13:45" > Next question
    """
    assert validate_time("13:45") == (13, 45)

def test_validate_time_invalid_format():
    """
    Test case for the validate_time() function.

    This test checks if the validate_time() function raises a ValueError
    when the input is not in the correct 24-hour format for time.

    Example:
        ("1:45") == "ValueError"
    Output: "13:45" == "Invalid time format! Please use HH:MM (24-hour)."
    """
    with pytest.raises(ValueError):
        validate_time("1:45 PM")


#Unit Tests for Latitude Validation
def test_validate_latitude_valid():
    """
    Test case for the validate_latitude() function.

    This test checks if the validate_latitude() functions correctly and accepts 
    the latitude input.

    Example:
        ("-37.8136") == "-37.8136"
    Output: "-37.8136" > Next question
    """
    assert validate_latitude("-37.8136") == -37.8136

def test_validate_latitude_invalid_format():
    """
    Test case for the validate_latitude() function.

    This test checks if the validate_latitude() raises a ValueError
    when the input is not in the correct number format for a latitude.

    Example:
        ("huvdbd") == "ValueError"
    Output: "Latitude must be a valid number with a decimal (e.g. -37.813629)"
    """
    with pytest.raises(ValueError):
        validate_latitude("NotANumber")

def test_validate_latitude_out_of_range():
    """
    Test case for the validate_latitude() function.

    This test checks if the validate_latitude() raises a ValueError
    when the input is not within the correct degrees.

    Example:
        ("200.0") == "ValueError"
    Output: ""Latitude must be between -90 and 90""
    """
    with pytest.raises(ValueError):
        validate_latitude("200.0")

def test_validate_latitude_empty_input():
    """
    Test case for the validate_latitude() function.

    This test checks if the validate_latitude() raises a ValueError
    when the input is empty.

    Example:
        ("") == "ValueError"
    Output: "Latitude must not be empty."
    """
    with pytest.raises(ValueError):
        validate_latitude("")

def test_validate_latitude_missing_decimal():
    """
    Test case for the validate_latitude() function.

    This test checks if the validate_latitude() raises a ValueError
    when the input is missing a decimal.

    Example:
        ("37") == "ValueError"
    Output: "Latitude must be a valid number with a decimal (e.g. -37.813629)"
    """
    with pytest.raises(ValueError):
        validate_latitude("37")


#Unit Tests for Longitude Validation
def test_validate_longitude_valid():
    """
    Test case for the validate_longitude() function.

    This test checks if the validate_longitude() functions correctly and accepts 
    the longitude input.

    Example:
        ("144.9631") == "144.9631"
    Output: "144.9631" > Next question
    """
    assert validate_longitude("144.9631") == 144.9631

def test_validate_longitude_invalid_format():
    """
    Test case for the validate_longitude() function.

    This test checks if the validate_longitude() raises a ValueError
    when the input is not in the correct number format for a longitude.

    Example:
        ("huvdbd") == "ValueError"
    Output: "Longitude must be a valid number with a decimal (e.g. 144.9631)"
    """
    with pytest.raises(ValueError):
        validate_longitude("NotANumber")

def test_validate_longitude_out_of_range():
    """
    Test case for the validate_longitude() function.

    This test checks if the validate_longitude() raises a ValueError
    when the input is not within the correct degrees.

    Example:
        ("200.0") == "ValueError"
    Output: ""Longitude must be between -90 and 90""
    """
    with pytest.raises(ValueError):
        validate_longitude("200.0")

def test_validate_longitude_empty_input():
    """
    Test case for the validate_longitude() function.

    This test checks if the validate_longitude() raises a ValueError
    when the input is empty.

    Example:
        ("") == "ValueError"
    Output: "Longitude must not be empty."
    """
    with pytest.raises(ValueError):
        validate_longitude("")

def test_validate_longitude_missing_decimal():
    """
    Test case for the validate_longitude() function.

    This test checks if the validate_longitude() raises a ValueError
    when the input is missing a decimal.

    Example:
        ("144") == "ValueError"
    Output: "Longitude must be a valid number with a decimal (e.g. -37.813629)"
    """
    with pytest.raises(ValueError):
        validate_longitude("144")


#Unit Tests for Timezone Validation
def test_valid_timezone():
    """
    Test case for the validate_timezone() function.

    This test checks if the validate_timezone() function correctly accepts the 
    timezone input.

    Example:
        ("Australia/Sydney") == "Australia/Sydney"
    Output: "Australia/Sydney" > Next question
    """
    assert validate_timezone("Australia/Sydney") == "Australia/Sydney"

@pytest.mark.xfail(reason="Expected to fail until fuzzy matching is implemented")
def test_forced_invalid_timezone():
    """
    Test case for the validate_timezone() function.

    This test checks if the validate_timezone() function causes a ValueError
    when the input is not an exact match to a timezone in pytz.all_timezones.

    Example:
        ("Australia/Syd") == "Invalid timezone"
    Output: "Australia/Sydney" > Next question
    """
    assert validate_timezone("Australia/Syd") == "Australia/Sydney"

def test_invalid_timezone_with_suggestion():
    """
    Test case for the validate_timezone() function.

    This test checks if the validate_timezone() provides a fuzzy match suggestion
    when the input is not an exact match to a timezone in pytz.all_timezones
    but is close enough to a valid timezone.

    Example:
        ("Australia/Melb") == "Australia/Melbourne"
    Output: ValueError: Did you mean: closest match (i.e. - Australia/Melbourne?)
    """
    with pytest.raises(ValueError) as exc_info:
        validate_timezone("Australia/Melb")
    assert "Did you mean:" in str(exc_info.value)

def test_invalid_timezone_no_match():
    """
    Test case for the validate_timezone() function.

    This test checks if the validate_timezone() function raises a ValueError for 
    timezones not in the pytz.all_timezones.

    Example:
        ("xyz") == (Invalid timezone)
    Output: "Invalid TImezone! Timezone must match a real timezone like Australia/Melbourne."
    """
    with pytest.raises(ValueError) as exc_info:
        validate_timezone("xyz")
    assert "Timezone must match a real timezone" in str(exc_info.value)
