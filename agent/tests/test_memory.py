from agent.collectors.memory import get_memory_usage


def test_memory_usage_returns_valid_percentage():
    memory = get_memory_usage()

    assert 0 <= memory <= 100