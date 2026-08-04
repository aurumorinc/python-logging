# src/python_logging/__init__.py
__version__ = "3.0.0"

import os
import sys

# Auto-instrumentation execution block
if not getattr(sys, "_LOGGING_INITIALIZED", False):
    setattr(sys, "_LOGGING_INITIALIZED", True)

    if os.environ.get("LOGGING_DISABLE_AUTO_INSTRUMENTATION", "").lower() != "true":
        try:
            from python_logging.service import setup

            setup()
        except Exception as e:
            sys.stderr.write(f"Auto-instrumentation failed: {e}\n")

# <AUTOGEN_INIT>
from python_logging import config
from python_logging import integrations
from python_logging import service

from python_logging.config import (
    LoggingSettings,
    generate_traceparent,
    resolve_traceparent,
    settings,
)
from python_logging.integrations import (
    get_windmill_traceparent,
    setup_structlog,
    structlog,
    windmill,
)
from python_logging.service import (
    add_otel_context,
    get_console_format,
    remove_otel_context,
    setup,
    setup_otel_provider,
)

__all__ = [
    "LoggingSettings",
    "add_otel_context",
    "config",
    "generate_traceparent",
    "get_console_format",
    "get_windmill_traceparent",
    "integrations",
    "remove_otel_context",
    "resolve_traceparent",
    "service",
    "settings",
    "setup",
    "setup_otel_provider",
    "setup_structlog",
    "structlog",
    "windmill",
]
# </AUTOGEN_INIT>
