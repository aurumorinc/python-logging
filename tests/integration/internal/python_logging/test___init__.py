import importlib
import sys
from unittest import mock

import python_logging


def test_package_integration_init():
    """Integration test verifying package root initialization."""
    with mock.patch("python_logging.service.setup"):
        if hasattr(sys, "_LOGGING_INITIALIZED"):
            delattr(sys, "_LOGGING_INITIALIZED")
        importlib.reload(python_logging)
        assert getattr(sys, "_LOGGING_INITIALIZED", False) is True
