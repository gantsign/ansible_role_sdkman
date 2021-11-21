Ansible Role: SDKMAN
====================

[![Tests](https://github.com/gantsign/ansible_role_sdkman/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_sdkman/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.sdkman-blue.svg)](https://galaxy.ansible.com/gantsign/sdkman)
[![License](https://img.shields.io/badge/license-Apache_2-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_sdkman/master/LICENSE)

Role to download and install [SDKMAN](https://sdkman.io/) the software
development kit manager.

Requirements
------------

* Ansible >= 2.8

* Linux Distribution

    * Debian Family

        * Debian

            * Stretch (9)
            * Buster (10)
            * Bullseye (11)

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

    * RedHat Family

        * Rocky Linux

            * 8

        * Fedora

            * 35

    * SUSE Family

        * openSUSE

            * 15.1

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# SDKMAN version number
sdkman_version: '5.13.1'

# The SHA256 of the SDKMAN redistributable package
sdkman_redis_sha256sum: '938bfd774e6c3b3564e0ed662189e683329675189d2ad7dd41d8d1ab02be0988'

# Directory to store files downloaded for SDKMAN
sdkman_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"

# SDKMAN is installed per user so you must specify at least one user
sdkman_users: []
# e.g.
# sdkman_users:
#   - example_username1
#   - example_username2
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.sdkman
      sdkman_users:
        - example_username
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

Apache 2

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
