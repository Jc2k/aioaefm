import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--integration",
        action="store_true",
        help="Run integration tests.",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "integration: mark test as an integration test")


def pytest_runtest_setup(item):
    isintegration = len(list(item.iter_markers(name="integration"))) > 0
    if isintegration:
        if not item.config.getoption("--integration"):
            pytest.skip("integration tests not selected in this run")
