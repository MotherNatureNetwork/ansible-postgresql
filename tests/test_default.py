def test_postgresql_service(Service):

    postgresql_service = Service('postgresql')

    assert postgresql_service.is_running
    assert postgresql_service.is_enabled
