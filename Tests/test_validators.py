"""
Test for Validators for Natal Chart Application  

"""
import pytest
from validators import (
    #validate_date,
    #validate_time,
    #validate_latitude,
    #validate_longitude,
    validate_timezone,
)

def test_valid_timezone():
    """
    Test case for the valid_timezone() function.

    This test checks if the valid_timezone() function correctly accepts the timezone input
    with correct input.

    Example:
        ("Australia/Sydney") == "Australia/Sydney"
    Output: "Australia/Sydney" > Next question
    """
    assert validate_timezone("Australia/Sydney") == "Australia/Sydney"


@pytest.mark.xfail(reason="Expected to fail until fuzzy matching is implemented")
def test_forced_invalid_timezone():
    """
    Test case for the valid_timezone() function.

    This test checks if the valid_timezone() function causes a ValueError
    when the input is not an exact match to a timezone in pytz.all_timezones.

    Example:
        ("Australia/Syd") == "Invalid timezone"
    Output: "Australia/Sydney" > Next question
    """
    assert validate_timezone("Australia/Syd") == "Australia/Sydney"


def test_invalid_timezone_with_suggestion():
    """
    Test case for the valid_timezone() function.

    This test checks if the valid_timezone() provides a fuzzy match suggestion
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
    Test case for the valid_timezone() function.

    This test checks if the valid_timezone() function raises a ValueError for 
    timezones not in the pytz.all_timezones.

    Example:
        ("xyz") == (Invalid timezone)
    Output: "Invalid TImezone! Timezone must match a real timezone like Australia/Melbourne."
    """
    with pytest.raises(ValueError) as exc_info:
        validate_timezone("xyz")
    assert "Timezone must match a real timezone" in str(exc_info.value)
