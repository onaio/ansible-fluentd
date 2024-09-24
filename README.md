onaio - Fluentd [![Build Status](https://github.com/onaio/ansible-fluentd/workflows/CI/badge.svg)](https://github.com/onaio/ansible-fluentd/actions?query=workflow%3ACI)
=========

Ansible role that installs and configures [Fluentd](https://docs.fluentd.org/) as a [ruby gem](https://docs.fluentd.org/installation/install-by-gem).

Requirements
------------

N/A

Role Variables
--------------

Check the [defaults/main.yml](./defaults/main.yml) file for the full list of default variables.

```yml
---
# fluentd version https://github.com/fluent/fluentd/releases
fluentd_version: "1.17.1"
fluentd_service_name: "fluentd"
fluentd_system_user: "fluentd"
fluentd_system_group: "fluentd"
fluentd_conf_directory: "/etc/fluent"
fluentd_conf_file: "fluent.conf"
fluentd_log_directory: "/var/log/fluent"
fluentd_log_file: "fluentd.log"
fluentd_lib_directory: "/opt/fluent/lib"
fluentd_gem_home_directory: "{{ fluentd_lib_directory }}"
fluentd_gem_path_directory: "{{ fluentd_lib_directory }}"
fluentd_system_environment_file: "/etc/environment"
fluentd_plugin_directory: "/etc/fluent/plugin"

fluentd_service_template: "etc/systemd/system/{{ fluentd_service_name }}.service.j2"
fluentd_service_path: "/etc/systemd/system/{{ fluentd_service_name }}.service"

# jemalloc https://github.com/jemalloc/jemalloc/releases confirm compatibility from dockerfile https://github.com/fluent/fluentd-docker-image
fluentd_jemalloc_version: "5.3.0"
fluentd_monitoring_groups:
  - adm

fluentd_extra_config_file_dir: "{{ fluentd_conf_directory }}/conf.d/ansible"

#  omitting version or using ">=0" will represent the latest version
fluentd_extra_plugins: []
#  - name: fluent-plugin-gelf
#  - name: fluent-plugin-influxdb
#    version: ">=0"

fluentd_configurations: []
#  - name: nginx-access-log
#    conf: |
#      <source>
#        @type tail
#        format nginx
#        pos_file /var/log/fluent/tmp/nginx-access.log.pos
#        tag nginx.access
#        path /var/log/nginx/access.log
#      </source>
#      <match nginx.access>
#        @type file
#        path /var/log/fluent/nginx-access
#      </match>
#  - name: syslog
#    conf: |
#      <source>
#        @type syslog
#        tag graylog2
#      </source>
#
#      <match graylog2.**>
#        @type gelf
#        host 127.0.0.1
#        port 12201
#        <buffer>
#          flush_interval 5s
#        </buffer>
#      </match>
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
      fluentd_configurations:
        - name: nginx-access-log
          conf: |
            <source>
              @type tail
              format nginx
              pos_file /var/log/fluent/tmp/nginx-access.log.pos
              tag nginx.access
              path /var/log/nginx/access.log
            </source>
            <match nginx.access>
              @type file
              path /var/log/fluent/nginx-access
            </match>
```

License
-------

Apache 2
