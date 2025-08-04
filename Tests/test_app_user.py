"""
Unit Testing for Class for Natal Chart Application  

"""
import re
import pytest
from main import AppUser

def strip_ansi(text):
    """Helper"""
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

@pytest.mark.usefixtures("capsys")
def test_app_user_creation():
    """TEST"""
    user = AppUser("Sam", 1990, 5, 10, 12, 30, "Melbourne", -37.8136, 144.9631, "Australia/Melbourne", "Australia")
    assert user.name == "Sam"
    assert user.latitude == -37.8136
    assert user.longitude == 144.9631


@pytest.mark.usefixtures("capsys")
def test_app_user_format_birth_data(capsys):
    """tEST"""
    user = AppUser("Alex", 2000, 1, 1, 14, 15, "Ballarat", -37.5, 143.8, "Australia/Melbourne", "Australia")
    user.format_birth_data()
    captured = capsys.readouterr()
    clean_output = strip_ansi(captured.out)
    assert "Name: Alex" in clean_output
    assert "Birth Date & Time: 2000-01-01 14:15" in clean_output
    assert "Birth Location: Ballarat (-37.5, 143.8)" in clean_output
    assert "Timezone: Australia/Melbourne" in clean_output
