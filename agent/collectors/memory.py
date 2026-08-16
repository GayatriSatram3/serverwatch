import psutil


def get_memory_usage() -> float:
    """
    Return the current memory utilization percentage.
    """
    memory = psutil.virtual_memory()
    return memory.percent