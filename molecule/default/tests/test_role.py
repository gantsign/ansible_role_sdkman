import pytest

import os

import testinfra.utils.ansible_runner

import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('dir_path', [
    '/home/test_usr1/.sdkman',
    '/home/test_usr1/.sdkman/bin',
    '/home/test_usr1/.sdkman/src',
    '/home/test_usr1/.sdkman/tmp',
    '/home/test_usr1/.sdkman/tmp/stage',
    '/home/test_usr1/.sdkman/ext',
    '/home/test_usr1/.sdkman/etc',
    '/home/test_usr1/.sdkman/var',
    '/home/test_usr1/.sdkman/archives',
    '/home/test_usr1/.sdkman/candidates',
    '/home/test_usr1/.sdkman-zsh',

])
def test_directories(host, dir_path):
    dir = host.file(dir_path)
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'test_usr1'
    assert dir.group in ['test_usr1', 'users']


@pytest.mark.parametrize('file_path', [
    '/home/test_usr1/.sdkman/bin/sdkman-init.sh',
    '/home/test_usr1/.sdkman/etc/config',
    '/home/test_usr1/.sdkman/src/sdkman-selfupdate.sh',
    '/home/test_usr1/.sdkman/src/sdkman-utils.sh',
    '/home/test_usr1/.sdkman/src/sdkman-availability.sh',
    '/home/test_usr1/.sdkman/src/sdkman-cache.sh',
    '/home/test_usr1/.sdkman/src/sdkman-update.sh',
    '/home/test_usr1/.sdkman/src/sdkman-upgrade.sh',
    '/home/test_usr1/.sdkman/src/sdkman-path-helpers.sh',
    '/home/test_usr1/.sdkman/src/sdkman-default.sh',
    '/home/test_usr1/.sdkman/src/sdkman-main.sh',
    '/home/test_usr1/.sdkman/src/sdkman-flush.sh',
    '/home/test_usr1/.sdkman/src/sdkman-current.sh',
    '/home/test_usr1/.sdkman/src/sdkman-install.sh',
    '/home/test_usr1/.sdkman/src/sdkman-use.sh',
    '/home/test_usr1/.sdkman/src/sdkman-broadcast.sh',
    '/home/test_usr1/.sdkman/src/sdkman-uninstall.sh',
    '/home/test_usr1/.sdkman/src/sdkman-offline.sh',
    '/home/test_usr1/.sdkman/src/sdkman-env-helpers.sh',
    '/home/test_usr1/.sdkman/src/sdkman-version.sh',
    '/home/test_usr1/.sdkman/src/sdkman-list.sh',
    '/home/test_usr1/.sdkman/src/sdkman-help.sh',
    '/home/test_usr1/.sdkman/var/version',
    '/home/test_usr1/.sdkman/var/candidates',
])
def test_files(host, file_path):
    installed_file = host.file(file_path)
    assert installed_file.exists
    assert installed_file.is_file
    assert installed_file.user == 'test_usr1'
    assert installed_file.group in ['test_usr1', 'users']


def test_version(host):
    cmd = ('sudo --user test_usr1 --login '
           'bash -c "source ~/.sdkmanrc && sdk version"')
    version = host.check_output(cmd)
    pattern = 'SDKMAN [0-9\\.\\+]+'
    assert re.search(pattern, version)
