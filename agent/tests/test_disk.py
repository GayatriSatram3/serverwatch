from agent.collectors.disk import get_disk_usage


def test_disk_usage_returns_valid_percentage():
    disk = get_disk_usage("/")

    assert 0 <= disk <= 100