import json
import socket
from datetime import datetime, timezone

from agent.collectors.cpu import get_cpu_usage
from agent.collectors.memory import get_memory_usage
from agent.collectors.disk import get_disk_usage
from agent.collectors.uptime import get_uptime_seconds
from agent.collectors.safe import safely_collect
from agent.status import determine_status


def collect_metrics() -> dict:
    """
    Collect all currently supported system metrics.
    """

    cpu = safely_collect(get_cpu_usage)
    memory = safely_collect(get_memory_usage)
    disk = safely_collect(lambda: get_disk_usage("/"))
    uptime = safely_collect(get_uptime_seconds)

    status = determine_status(cpu, memory, disk)

    return {
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "cpu_percent": cpu,
        "memory_percent": memory,
        "disk_percent": disk,
        "uptime_seconds": uptime,
    }


if __name__ == "__main__":
    metrics = collect_metrics()

    print(json.dumps(metrics, indent=2))