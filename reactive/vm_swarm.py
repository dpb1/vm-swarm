from charms.reactive import when, when_not, set_state
from charmhelpers.core import hookenv
from charmhelpers import fetch
import subprocess


@when_not('vm-swarm.installed')
def install_vm_swarm():
    install_packages()
    setup_vms()
    hookenv.status_set('maintenance', 'Installed')
    set_state('vm-swarm.installed')

def setup_vms():
    cfg = hookenv.config()
    subprocess.check_call(["./add-vms", cfg["maas-url"], cfg["maas-oauth"]])

def install_packages():
    hookenv.status_set('maintenance', 'Installing packages')
    fetch.apt_update()
    packages = ['maas-cli', 'virtinst', 'kvm']
    fetch.apt_install(fetch.filter_installed_packages(packages))
