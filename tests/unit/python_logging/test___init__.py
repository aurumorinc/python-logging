import importlib
import os
import sys
from unittest import mock

import pytest

import python_logging


@pytest.fixture(autouse=True)
def reset_logging_init_state():
    """Reset the module-level state before and after each test."""
    if hasattr(sys, "_LOGGING_INITIALIZED"):
        delattr(sys, "_LOGGING_INITIALIZED")
    yield
    if hasattr(sys, "_LOGGING_INITIALIZED"):
        delattr(sys, "_LOGGING_INITIALIZED")


@mock.patch.dict(os.environ, {"LOGGING_DISABLE_AUTO_INSTRUMENTATION": "true"})
@mock.patch("python_logging.service.setup")
def test_init_disabled_via_env(mock_setup):
    """Test that setting LOGGING_DISABLE_AUTO_INSTRUMENTATION disables setup."""
    importlib.reload(python_logging)
    mock_setup.assert_not_called()
    assert getattr(sys, "_LOGGING_INITIALIZED", False) is True


@mock.patch.dict(os.environ, {"LOGGING_DISABLE_AUTO_INSTRUMENTATION": "false"})
@mock.patch("python_logging.service.setup")
def test_init_executes_setup(mock_setup):
    """Test that setup is called on import."""
    importlib.reload(python_logging)
    mock_setup.assert_called_once()
    assert getattr(sys, "_LOGGING_INITIALIZED", False) is True


@mock.patch.dict(os.environ, {"LOGGING_DISABLE_AUTO_INSTRUMENTATION": "false"})
@mock.patch("python_logging.service.setup")
def test_init_catches_setup_exceptions(mock_setup):
    """Test that exceptions during setup are caught and do not crash."""
    mock_setup.side_effect = Exception("Test exception")

    with mock.patch("sys.stderr.write") as mock_stderr:
        importlib.reload(python_logging)
        mock_setup.assert_called_once()
        mock_stderr.assert_called_once_with(
            "Auto-instrumentation failed: Test exception\n"
        )
        assert getattr(sys, "_LOGGING_INITIALIZED", False) is True


@mock.patch("python_logging.service.setup")
def test_init_idempotency(mock_setup):
    """Test that initialization only occurs once."""
    setattr(sys, "_LOGGING_INITIALIZED", True)

    importlib.reload(python_logging)
    mock_setup.assert_not_called()
