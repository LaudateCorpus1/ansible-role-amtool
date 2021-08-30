import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_amtool_installed(host):
    test_bin_dir = host.file("/tmp/bin")
    test_amtool = host.file("/tmp/bin/amtool")

    assert test_bin_dir.is_directory
    assert test_amtool.is_file
    assert test_amtool.mode == 0o0755
