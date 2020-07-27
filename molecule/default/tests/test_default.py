import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_td_agent_service(host):
    td_agent_service = host.service("td-agent")

    assert td_agent_service.is_running
    assert td_agent_service.is_enabled


def test_td_agent_user_added_to_monitoring_group(host):
    td_agent_user = host.user("td-agent")

    assert "adm" in td_agent_user.groups


def test_td_agent_configuration(host):
    td_agent_conf_file = host.file("/etc/td-agent/td-agent.conf")
    expected_conf_content = """####
## Source descriptions:
##

<source>
    @type tail
    path /var/log/nginx/*
    pos_file /var/log/td-agent/pos/nginx_log.pos
    tag s3.nginx
    read_from_head true

    <parse>
        @type none
    </parse>
</source>

####
## Filter descriptions:
##

<filter s3.*>
    @type record_transformer
    <record>
        hostname "#{Socket.gethostname}"
        tag ${tag}
    </record>
</filter>

####
## Match descriptions:
##

<match s3.*>
    @type s3
    aws_key_id test_key_id
    aws_sec_key test_secret_key
    s3_bucket test-bucket
    s3_region eu-west-1
    path ona/test/${tag}/
    s3_object_key_format %{path}%{time_slice}_%{index}.%{file_extension}
    store_as gzip

    <buffer tag,time>
        @type file
        path /var/log/td-agent/s3
        timekey 30m
        timekey_wait 10m
        timekey_use_utc true
        flush_at_shutdown true
    </buffer>
</match>
"""

    assert td_agent_conf_file.content_string == expected_conf_content
