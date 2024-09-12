# test_error.py
import pytest

# Passing test


def test_syntax_error():
    with pytest.raises(TypeError):
        # Importing the file should raise a TypeError due to the last line
        __import__("error")

# Failing test, the program should not be able to print out "3" because of the type error


def test_correct_lines(capsys):
    # Test the console output
    captured = capsys.readouterr()
    assert "3" in captured.out
