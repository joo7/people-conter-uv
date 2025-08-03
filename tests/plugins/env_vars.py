import os 
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    os.environ.setdefault("API_KEY", "test-api-key")
    os.environ.setdefault("ENV", "test")