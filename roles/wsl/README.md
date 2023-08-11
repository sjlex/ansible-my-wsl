wsl
=========

An Ansible role to configure wsl.

Requirements
------------

None

Role Variables
--------------

`wsl_user_name`: WSL user name

`wsl_memory`: WSL2 memory (default: "4GB")

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.wsl, wsl_memory: "8GB" }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
