from charms.reactive import when, when_not, set_state
from charmhelpers.core import hookenv
from charmhelpers import fetch


@when_not('vm-swarm.installed')
def install_vm_swarm():
    install_packages()
    set_state('vm-swarm.installed')

def install_packages():
    hookenv.status_set('maintenance', 'Installing packages')
    #fetch.add_source('ppa:...')
    fetch.apt_update()
    packages = ['maas-cli', 'virtinst', 'kvm']
    fetch.apt_install(fetch.filter_installed_packages(packages))
