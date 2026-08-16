from typing import Callable, Any


def safely_collect(collector: Callable[[], Any]) -> Any:
    """
    Execute a collector and return None if it fails.
    """
    try:
        return collector()
    except Exception:
        return None