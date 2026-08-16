from agent.collectors.cpu import get_cpu_usage


def test_cpu_usage_returns_valid_percentage():
    cpu = get_cpu_usage()

    assert 0 <= cpu <= 100