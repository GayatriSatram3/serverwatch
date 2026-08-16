import psutil


def get_disk_usage(path: str = "/") -> float:
    """
    Return disk utilization percentage for the given path.
    """
    disk = psutil.disk_usage(path)
    return disk.percent