import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgresql_running_and_enabled(host):
    psql = host.service("postgresql")
    assert psql.is_running
    assert psql.is_enabled
