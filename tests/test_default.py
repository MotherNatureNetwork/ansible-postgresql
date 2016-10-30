from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory')\
                  .get_hosts('all')


def test_postgresql_service(Service):

    postgresql_service = Service('postgresql')

    assert postgresql_service.is_running
    assert postgresql_service.is_enabled
