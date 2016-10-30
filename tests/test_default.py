def test_postgresql_service(Service):

    postgresql_service = Service('postgresql')

    assert postgresql_service.is_running
    assert postgresql_service.is_enabled


def test_postgresql_database(Command):

    cmd = Command("psql")

    assert cmd.rc == 0
