import time
import psutil


def get_uptime_seconds() -> float:
    """
    Return the number of seconds the system has been running.
    """
    return time.time() - psutil.boot_time()