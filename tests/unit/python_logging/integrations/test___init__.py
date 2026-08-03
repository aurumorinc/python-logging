import python_logging.integrations as integrations_pkg


def test_integrations_exports():
    """Test that python_logging.integrations exports expected functions and modules."""
    assert hasattr(integrations_pkg, "get_windmill_traceparent")
    assert hasattr(integrations_pkg, "setup_structlog")
    assert hasattr(integrations_pkg, "structlog")
    assert hasattr(integrations_pkg, "windmill")

    assert "get_windmill_traceparent" in integrations_pkg.__all__
    assert "setup_structlog" in integrations_pkg.__all__
    assert "structlog" in integrations_pkg.__all__
    assert "windmill" in integrations_pkg.__all__
