Ansible Role: SDKMAN
====================

[![Build Status](https://travis-ci.com/gantsign/ansible_role_sdkman.svg?branch=master)](https://travis-ci.com/gantsign/ansible_role_sdkman)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.sdkman-blue.svg)](https://galaxy.ansible.com/gantsign/sdkman)
[![License](https://img.shields.io/badge/license-Apache_2-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_sdkman/master/LICENSE)

Role to download and install [SDKMAN](https://sdkman.io/) the software
development kit manager.

Requirements
------------

* Ansible >= 2.4

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

        * Fedora

            * 28

    * SUSE Family

        * openSUSE

            * 15.0

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# SDKMAN version number
sdkman_version: '5.7.2+323'

# The SHA256 of the SDKMAN redistributable package
sdkman_redis_sha256sum: '171ae6a3b4d4f0dd88e5e812943ca9b8f887fe78ddafa3b8a2f8b508472a9efa'

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

Tab Completion for Zsh
----------------------

### Using Ansible

The recommended way to enable Zsh support for SDKMAN is to use the
[gantsign.antigen](https://galaxy.ansible.com/gantsign/antigen) role (this must
be configured for each user).


```yaml
- hosts: servers
  roles:
    - role: gantsign.sdkman
      sdkman_users:
        - example_username

    - role: gantsign.antigen
      users:
        - username: example_username
          antigen_bundles:
            - name: sdkman
              url: '$HOME/.sdkman-zsh'
```

### Using Antigen

If you prefer to use [Antigen](https://github.com/zsh-users/antigen) directly
add the following to your Antigen configuration:

```bash
antigen bundle ~/.sdkman-zsh
```

### Manual configuration

To manually configure Zsh add the following to your `.zshrc`:

```bash
# Configure tab completion for SDKMAN
fpath=(~/.sdkman-zsh $fpath)
autoload -U compinit && compinit
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

To test this role run the following command from the project root:

```bash
molecule test
```

License
-------

Apache 2

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
