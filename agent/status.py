def determine_status(
    cpu_percent: float | None,
    memory_percent: float | None,
    disk_percent: float | None,
) -> str:

    values = [cpu_percent, memory_percent, disk_percent]

    if any(value is None for value in values):
        return "UNKNOWN"

    if any(value >= 90 for value in values):
        return "CRITICAL"

    if any(value >= 80 for value in values):
        return "WARNING"

    return "HEALTHY"