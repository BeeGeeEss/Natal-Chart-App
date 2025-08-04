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

    This test checks if the valid_timezone() function correctly accepts the timezone input.

    Example:
        >>> assert valid_timezone("Australia/Sydney") == "Australia/Sydney"
    """
    assert validate_timezone("Australia/Sydney") == "Australia/Sydney"


def test_forced_invalid_timezone():
    """
    Test case for the valid_timezone() function.

    This test checks if the valid_timezone() function provides an error warning if the spelling is slightly incorrect.
    This test is intended to fail - to provide an opportunity for Test Driven Development.

    Example:
        >>> assert valid_timezone("Australia/Sydney") == "Australia/Sydney"
    """
    assert validate_timezone("Aus/Sydney") == "Australia/Sydney"


def test_invalid_timezone():
    """
    Test case for the valid_timezone() function.

    This test checks if the valid_timezone() function raises a ValueError if the timezone is not in the pytz.all_timezones.

    Example:
        >>> assert valid_timezone("Australia/Sydney") == "Australia/Sydney"
    """
    with pytest.raises(ValueError):
        validate_timezone("Not/ARealPlace")
