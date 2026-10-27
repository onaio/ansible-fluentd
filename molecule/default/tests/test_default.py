import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_td_agent_service(host):
    td_agent_service = host.service("fluentd")

    assert td_agent_service.is_running
    assert td_agent_service.is_enabled


def test_td_agent_user_added_to_monitoring_group(host):
    td_agent_user = host.user("fluentd")

    assert "adm" in td_agent_user.groups


def test_td_agent_configuration(host):
    td_agent_conf_file = host.file("/etc/fluent/fluent.conf")
    header, body = td_agent_conf_file.content_string.split("\n", 1)
    expected_body = """
@include "/etc/fluent/conf.d/ansible/nginx-access-log.conf"

"""

    # The header wording depends on the ansible-core version
    assert header.startswith("# Ansible managed")
    assert body == expected_body
