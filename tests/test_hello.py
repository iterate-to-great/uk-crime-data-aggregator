"""Unit tests for hello module."""

import pytest

from src.hello import greet, main


class TestGreet:
    """Tests for the greet function."""

    def test_greet_default(self) -> None:
        """Test greet with default parameter."""
        assert greet() == "Hello, World!"

    def test_greet_with_name(self) -> None:
        """Test greet with custom name."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_with_empty_string(self) -> None:
        """Test greet with empty string."""
        assert greet("") == "Hello, !"

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Python", "Hello, Python!"),
            ("Developer", "Hello, Developer!"),
            ("123", "Hello, 123!"),
        ],
    )
    def test_greet_parametrized(self, name: str, expected: str) -> None:
        """Test greet with multiple inputs using parametrize."""
        assert greet(name) == expected


class TestMain:
    """Tests for the main function."""

    def test_main_prints_greeting(self, capsys: pytest.CaptureFixture) -> None:
        """Test that main prints the default greeting."""
        main()
        captured = capsys.readouterr()
        assert captured.out == "Hello, World!\n"
