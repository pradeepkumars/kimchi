#
# Project Burnet
#
# Copyright IBM, Corp. 2013
#
# Authors:
#  Adam Litke <agl@linux.vnet.ibm.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import copy

osinfo = [
    ('unknown', {
        'version': lambda d,v: True,
        'icon': 'images/icon-vm.svg',
        'os_distro': 'unknown', 'os_version': 'unknown',
        'cpus': 1, 'cpu_cores': 1, 'cpu_threads': 1,
        'memory': 1024,
        'cdrom': '',
        'disks': [{'index': 0, 'size': 10}],
        'disk_bus': 'ide', 'nic_model': 'ne2k_pci',
        'cdrom_bus': 'ide', 'cdrom_index': 2,
    }),
    ('debian', {
        'version': lambda d,v: bool(d == 'debian' and v in ('squeeze',)),
        'icon': 'images/icon-debian.png',
        'cpus': 1, 'cpu_cores': 1, 'cpu_threads': 1,
        'memory': 1024,
        'disks': [{'index': 0, 'size': 10}],
        'disk_bus': 'virtio', 'nic_model': 'virtio',
        'cdrom_bus': 'ide', 'cdrom_index': 2,
    }),
    ('ubuntu', {
        'version': lambda d,v: bool(d == 'ubuntu' and v in ('raring',)),
        'icon': 'images/icon-ubuntu.png',
        'cpus': 1, 'cpu_cores': 1, 'cpu_threads': 1,
        'memory': 1024,
        'disks': [{'index': 0, 'size': 10}],
        'disk_bus': 'virtio', 'nic_model': 'virtio',
        'cdrom_bus': 'ide', 'cdrom_index': 2,
    }),
    ('opensuse-12.3', {
        'version': lambda d,v: bool(d == 'opensuse' and v in ('12.3',)),
        'icon': 'images/icon-opensuse.png',
        'cpus': 1, 'cpu_cores': 1, 'cpu_threads': 1,
        'memory': 1024,
        'disks': [{'index': 0, 'size': 10}],
        'disk_bus': 'virtio', 'nic_model': 'virtio',
        'cdrom_bus': 'ide', 'cdrom_index': 2,
    }),
    ('fedora-18', {
        'version': lambda d,v: bool(d == 'fedora' and v in ('16', '17', '18',)),
        'icon': 'images/icon-fedora.png',
        'cpus': 1, 'cpu_cores': 1, 'cpu_threads': 1,
        'memory': 1024,
        'disks': [{'index': 0, 'size': 10}],
        'disk_bus': 'virtio', 'nic_model': 'virtio',
        'cdrom_bus': 'ide', 'cdrom_index': 2,
    }),
]

isolinks = {
    'debian': {
        'squeeze': 'http://cdimage.debian.org/debian-cd/6.0.7-live/amd64/iso-hybrid/debian-live-6.0.7-amd64-gnome-desktop.iso',
    },
    'ubuntu': {
        'raring': 'http://ubuntu-releases.cs.umn.edu/13.04/ubuntu-13.04-desktop-amd64.iso',
    },
    'opensuse': {
        '12.3': 'http://suse.mirrors.tds.net/pub/opensuse/distribution/12.3/iso/openSUSE-12.3-DVD-x86_64.iso',
    },
    'fedora': {
        '16': 'http://fedora.mirrors.tds.net/pub/fedora/releases/16/Live/x86_64/Fedora-16-x86_64-Live-Desktop.iso',
        '17': 'http://fedora.mirrors.tds.net/pub/fedora/releases/17/Live/x86_64/Fedora-17-x86_64-Live-Desktop.iso',
        '18': 'http://fedora.mirrors.tds.net/pub/fedora/releases/18/Live/x86_64/Fedora-18-x86_64-Live-Desktop.iso',
    },
}

defaults = {'network': 'default', 'storagepool': '/storagepools/default'}

def lookup(distro, version):
    ret = None
    for name, entry in osinfo:
        # Test if this entry is a valid match
        if entry['version'](distro, version):
            params = copy.copy(entry)
            params['cdrom'] = isolinks.get(distro, {}).get(version, '')
            del params['version']  # Don't pass around the version function
            ret = (name, params)
    if ret:
        ret[1].update(defaults)
    return ret
