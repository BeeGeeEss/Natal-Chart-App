"""
Unit Testing for Validators for Natal Chart Application  

"""

# ========================================
# Natal Chart Generator - Validator Unit Tests
# ========================================

# --- Third-Party Imports ---
import pytest
from validators import (
    validate_date,
    validate_time,
    validate_latitude,
    validate_longitude,
    validate_timezone,
)


# -------------------------------
# Unit Tests for Date Validation
# -------------------------------

def test_validate_date_valid():
    """Accepts a valid YYYY-MM-DD date"""
    assert validate_date("2020-01-15") == (2020, 1, 15)

def test_validate_date_invalid_format():
    """Rejects incorrectly formatted date (e.g. DD-MM-YYYY)"""
    with pytest.raises(ValueError):
        validate_date("15-01-2020")

def test_validate_date_invalid_d_m_format():
    """Rejects impossible date values (e.g. month 30)"""
    with pytest.raises(ValueError):
        validate_date("2000-30-05")



# -------------------------------
# Unit Tests for Time Validation
# -------------------------------

def test_validate_time_valid():
    """Accepts valid 24-hour time format"""
    assert validate_time("13:45") == (13, 45)

def test_validate_time_invalid_format():
    """Rejects non-24-hour time format (e.g. '1:45 PM')"""
    with pytest.raises(ValueError):
        validate_time("1:45 PM")



# -------------------------------
# Unit Tests for Latitude Validation
# -------------------------------

def test_validate_latitude_valid():
    """Accepts a valid latitude value"""
    assert validate_latitude("-37.8136") == -37.8136

def test_validate_latitude_invalid_format():
    """Rejects non-numeric latitude input"""
    with pytest.raises(ValueError):
        validate_latitude("NotANumber")

def test_validate_latitude_out_of_range():
    """Rejects latitude outside valid range (-90 to 90)"""
    with pytest.raises(ValueError):
        validate_latitude("200.0")

def test_validate_latitude_empty_input():
    """Rejects empty latitude input"""
    with pytest.raises(ValueError):
        validate_latitude("")

def test_validate_latitude_missing_decimal():
    """Rejects latitude without decimal point"""
    with pytest.raises(ValueError):
        validate_latitude("37")



# # -------------------------------
# # Unit Tests for Longitude Validation
# # -------------------------------

def test_validate_longitude_valid():
    """Accepts a valid longitude value"""
    assert validate_longitude("144.9631") == 144.9631

def test_validate_longitude_invalid_format():
    """Rejects non-numeric longitude input"""
    with pytest.raises(ValueError):
        validate_longitude("NotANumber")

def test_validate_longitude_out_of_range():
    """Rejects longitude outside valid range (-180 to 180)"""
    with pytest.raises(ValueError):
        validate_longitude("200.0")

def test_validate_longitude_empty_input():
    """Rejects empty longitude input"""
    with pytest.raises(ValueError):
        validate_longitude("")

def test_validate_longitude_missing_decimal():
    """Rejects longitude without decimal point"""
    with pytest.raises(ValueError):
        validate_longitude("144")



# -------------------------------
# Unit Tests for Timezone Validation
# -------------------------------

def test_valid_timezone():
    """Accepts a valid timezone"""
    assert validate_timezone("Australia/Sydney") == "Australia/Sydney"

@pytest.mark.xfail(reason="Expected to fail until fuzzy matching is implemented")
def test_forced_invalid_timezone():
    """Fails on partial timezone without fuzzy matching"""
    assert validate_timezone("Australia/Syd") == "Australia/Sydney"

def test_invalid_timezone_with_suggestion():
    """Provides fuzzy match suggestion for near-valid timezone"""
    with pytest.raises(ValueError) as exc_info:
        validate_timezone("Australia/Melb")
    assert "Did you mean:" in str(exc_info.value)

def test_invalid_timezone_no_match():
    """Provides fuzzy match suggestion for near-valid timezone"""
    with pytest.raises(ValueError) as exc_info:
        validate_timezone("xyz")
    assert "Timezone must match a real timezone" in str(exc_info.value)
