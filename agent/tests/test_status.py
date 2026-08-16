from agent.status import determine_status


def test_healthy_status():
    assert determine_status(30, 40, 50) == "HEALTHY"


def test_warning_status():
    assert determine_status(85, 40, 50) == "WARNING"


def test_critical_status():
    assert determine_status(95, 40, 50) == "CRITICAL"


def test_unknown_status():
    assert determine_status(None, 40, 50) == "UNKNOWN"