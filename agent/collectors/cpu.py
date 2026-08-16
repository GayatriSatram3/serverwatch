import psutil


def get_cpu_usage() -> float:
    """
    Return the current CPU utilization percentage.
    """
    return psutil.cpu_percent(interval=1.0)