import python_logging.integrations as integrations_pkg


def test_integrations_subpackage_integration():
    """Integration test verifying integrations subpackage imports and exports."""
    assert integrations_pkg.get_windmill_traceparent is not None
    assert integrations_pkg.setup_structlog is not None
