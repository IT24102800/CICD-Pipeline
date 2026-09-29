import pytest
from app import (
    validate_username,
    create_profile_message,
    generate_reset_code,
    show_directory_contents,
)


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


def test_reset_code_is_string():
    assert isinstance(generate_reset_code(), str)


def test_reset_code_has_six_digits():
    code = generate_reset_code()
    assert len(code) == 6
    assert code.isdigit()


def test_show_directory_contents_lists_entries(tmp_path, monkeypatch, capsys):
    (tmp_path / "alpha.txt").write_text("a", encoding="utf-8")
    (tmp_path / ".hidden").write_text("b", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    show_directory_contents()
    output_lines = capsys.readouterr().out.splitlines()

    assert output_lines == [".hidden", "alpha.txt"]