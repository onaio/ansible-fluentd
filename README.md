onaio - Fluentd [![Build Status](https://github.com/onaio/ansible-fluentd/workflows/CI/badge.svg)](https://github.com/onaio/ansible-fluentd/actions?query=workflow%3ACI)
=========

Ansible role that installs and configures Fluentd. This role installs `td-agent`. See [differences between td-agent and Fluentd here](https://www.fluentd.org/faqs).

Requirements
------------

N/A

Role Variables
--------------

Check the [defaults/main.yml](./defaults/main.yml) file for the full list of default variables.

```yml
---
# version of td-agent
fluentd_td_version: "4"
# name of the td-agent service
fluentd_service_name: "td-agent"
# system user for td-agent service
fluentd_system_user: "td-agent"
# list of groups to add the td-agent user to
fluentd_monitoring_groups:
  - adm

# input config
# directory to store the last read position of a log
fluentd_source_log_pos_directory: "/var/log/td-agent"
# log paths to tail
fluentd_log_paths:
  - tag: "nginx"
    path: "/var/log/nginx/*"

# output config
fluentd_aws_key_id: ""
fluentd_aws_secret_key: ""
fluentd_s3_bucket: "logs"
fluentd_s3_region: ""
fluentd_server_owner: ""
fluentd_server_environment: ""
fluentd_s3_buffer_file_path: "/var/log/td-agent/s3"
fluentd_s3_buffer_timekey: "30m"
fluentd_s3_buffer_timekey_wait: "10m"
```

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yml
- hosts: servers
  roles:
    - role: ansible-fluentd
      fluentd_monitoring_groups:
        - adm
      fluentd_log_paths:
        - tag: auth
          path: /var/log/auth.log*
        - tag: syslog
          path: /var/log/syslog*
      fluentd_aws_key_id: test_key_id
      fluentd_aws_secret_key: test_secret_key
      fluentd_s3_bucket: test-bucket
      fluentd_s3_region: eu-west-1
      fluentd_server_owner: ona
      fluentd_server_environment: test
```

License
-------

Apache 2
