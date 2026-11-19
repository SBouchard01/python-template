"""The base module of the package."""


def hello_world() -> str:
    """Return a greeting message."""
    return "Hello, World!"


def uncovered_function(x: int) -> int: # Mismatched return type flagged by ty
    """Uncovered by tests, and with mismatched return type."""
    # Artificially increase cyclomatic complexity to trigger a failed CRAP score
    if x > 100: # PLR2004 flagged by ruff
        return "big"
    elif x > 10: # RET505 flagged by ruff
        return "medium"
    elif x > 0:
        return "small"
    return "This function is not covered by tests."
