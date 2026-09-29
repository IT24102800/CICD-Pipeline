import pytest
from app import validate_username, create_profile_message

def test_valid_username():
    assert validate_username("student_01") is True

def test_short_username():
    assert validate_username("abc") is False

def test_username_with_invalid_symbol():
    assert validate_username("student@01") is False

def test_profile_message():
    result = create_profile_message("student_01", "student")
    assert result == "User: student_01 | Role: student"

def test_invalid_role():
    with pytest.raises(ValueError):
        create_profile_message("student_01", "superuser")