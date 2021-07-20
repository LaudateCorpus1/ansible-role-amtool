Ansible role ableton.amtool
===========================

This role installs [`amtool`][amtool] (from [alertmanager][alertmanager]) on the Ansible
control host (note: this is the machine that you run your playbooks on, **not** the host
which you are provisioning with Ansible). The purpose of this role is to make `amtool`
available on the control host in order to create and expire silences.

Requirements
------------

Ansible >= 2.10, and a control host which is either running a Debian-flavor of Linux, or
macOS.

Role Variables
--------------

See the [`defaults/main.yml`](defaults/main.yml) file for full documentation on required
and optional role variables.

After the role installs `amtool`, it will set the `amtool_exe` fact to the path of the
installed executable. This fact can be used to call `amtool` from subsequent `command`
tasks in your playbooks. Note that such tasks must be delegated to `localhost`.

Example Playbook
----------------

```yaml
---
- name: Create alert silences for all hosts
  hosts: "all"
  gather_facts: false
  vars:
    alertmanager_url: "https://example.com/alertmanager"
    comment: "Added by Ansible"
    expiration_timeout: "4h"

  roles:
    - role: ableton.amtool
      run_once: true

  tasks:
    - name: Create silences for example alerts
      delegate_to: localhost
      command: "{{ amtool_exe }} \
        --alertmanager.url={{ alertmanager_url }} \
        silence add \
        --comment='{{ comment }}' \
        --duration={{ expiration_timeout }} \
        alertname={{ alert_item }}"
      loop_control:
        loop_var: alert_item
      with_items:
        - "example_alert_one"
        - "example_alert_two"
```

License
-------

MIT

Maintainers
-----------

This project is maintained by the following GitHub users:

- [@ala-ableton](https://github.com/ala-ableton)
- [@nre-ableton](https://github.com/nre-ableton)


[alertmanager]: https://www.prometheus.io/docs/alerting/latest/alertmanager/
[amtool]: https://manpages.debian.org/buster/prometheus-alertmanager/amtool.1.en.html
