import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_install(host):
    install_location = host.run('/opt/graalvm-ce/bin/java -version')
    assert 'GraalVM CE' in install_location.stderr

