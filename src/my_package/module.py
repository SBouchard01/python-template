"""The base module of the package."""


def hello_world() -> str:
    """Return a greeting message."""
    return "Hello, World!"
# This line should be reformatted by ruff
def uncovered_function() -> int:
    """Uncovered by tests, and with mismatched return type."""
    return "This function is not covered by tests." # flagged by ty
