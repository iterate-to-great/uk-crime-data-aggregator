"""Simple hello world module."""


def greet(name: str = "World") -> str:
    """
    Return a greeting message.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Main entry point."""
    print(greet())


if __name__ == "__main__":
    main()
