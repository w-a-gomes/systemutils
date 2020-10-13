#!/usr/bin/env python3
# https://github.com/w-a-gomes/osutility
import subprocess
import re


class OsInfo(object):
    """Create an object of type 'OsInfo'"""
    def __init__(self):
        """Class constructor"""
        self.__current_user = str()
        self.__current_username = str()
        self.__hostname = str()
        self.__all_release_info = dict()
        self.__pretty_name = str()
        self.__name = str()
        self.__name_id = str()
        self.__codename = str()
        self.__version = str()
        self.__kernel = str()
        self.__kernel_version = str()
        self.__architecture = str()
        self.__motherboard = str()
        self.__cpu = str()
        self.__gpu = str()
        self.__ram = str()
        self.__swap = str()
        self.__screen_resolution = str()
        self.__uptime = str()
        self.__shell = str()
        self.__desktop_environment = str()
        self.__window_manager = str()
        self.__deb_packages = str()
        self.__flatpak_packages = str()
        self.__snap_packages = str()
        self.__font = str()
        self.__browser = str()

        self.get_all_release_info()

    def get_current_username(self):
        if self.__current_username:
            return self.__current_username

        self.__current_username = subprocess.getoutput('echo $USER')
        return self.__current_username

    def get_current_user(self):
        if self.__current_user:
            return self.__current_user

        self.__current_user = subprocess.getoutput(
            "cat /etc/passwd | grep `whoami` | awk -F ',' '{print $1}' | awk -F ':' '{print $5}'")

        return self.__current_user

    def get_hostname(self):
        if self.__hostname:
            return self.__hostname

        # Fix $HOSTNAME missing
        if subprocess.getoutput('cat /etc/hostname ; echo $?')[-1] == '0':
            hostname = subprocess.getoutput('cat /etc/hostname')
        else:
            hostname = subprocess.getoutput('echo $HOSTNAME')

        # Fix $HOSTNAME in Fedora
        if 'fedora' in self.get_name().lower():
            hostname = subprocess.getoutput('printf "${HOSTNAME%%.*}"')

        self.__hostname = hostname
        return self.__hostname

    def get_all_release_info(self):
        if self.__all_release_info:
            return self.__all_release_info

        cat_release = subprocess.getoutput('cat /etc/os-release').split('\n')
        for item_release in cat_release:
            items = item_release.split('=')
            self.__all_release_info[items[0]] = items[1].strip('"').strip("'")

        return self.__all_release_info

    def get_pretty_name(self):
        if self.__pretty_name:
            return self.__pretty_name

        if 'PRETTY_NAME' in self.__all_release_info:
            self.__pretty_name = self.__all_release_info['PRETTY_NAME']

        return self.__pretty_name

    def get_name(self):
        if self.__name:
            return self.__name

        if 'NAME' in self.__all_release_info:
            self.__name = self.__all_release_info['NAME']
        return self.__name

    def get_name_id(self):
        if self.__name_id:
            return self.__name_id

        if 'ID' in self.__all_release_info:
            self.__name_id = self.__all_release_info['ID']
        elif 'NAME' in self.__all_release_info:
            self.__name_id = self.__all_release_info['NAME'].lower()

        return self.__name_id

    def get_codename(self):
        if self.__codename:
            return self.__codename

        if 'VERSION_CODENAME' in self.__all_release_info:
            self.__codename = self.__all_release_info['VERSION_CODENAME']
        elif 'CODENAME' in self.__all_release_info:
            self.__codename = self.__all_release_info['CODENAME']

        return self.__codename

    def get_version(self):
        if self.__version:
            return self.__version

        if 'VERSION_ID' in self.__all_release_info:
            self.__version = self.__all_release_info['VERSION_ID']
        elif 'VERSION' in self.__all_release_info:
            self.__version = self.__all_release_info['VERSION']

        return self.__version

    def get_kernel(self):
        if self.__kernel:
            return self.__kernel

        self.__kernel = subprocess.getoutput('cat /proc/sys/kernel/ostype').title()
        return self.__kernel

    def get_kernel_version(self):
        if self.__kernel_version:
            return self.__kernel_version

        regex = re.compile(r'(\.x\d.+|x\d.+)')
        self.__kernel_version = regex.sub(
            '', subprocess.getoutput('cat /proc/sys/kernel/osrelease'))

        return self.__kernel_version

    def get_architecture(self):
        if self.__architecture:
            return self.__architecture

        self.__architecture = subprocess.getoutput('getconf LONG_BIT').title()
        return self.__architecture

    def get_motherboard(self):
        if self.__motherboard:
            return self.__motherboard

    def get_cpu(self):
        if self.__cpu:
            return self.__cpu

    def get_gpu(self):
        if self.__gpu:
            return self.__gpu

    def get_ram(self):
        if self.__ram:
            return self.__ram

    def get_swap(self):
        if self.__swap:
            return self.__swap

    def get_screen_resolution(self):
        if self.__screen_resolution:
            return self.__screen_resolution

    def get_uptime(self):
        if self.__uptime:
            return self.__uptime

    def get_shell(self):
        if self.__shell:
            return self.__shell

    def get_desktop_environment(self):
        if self.__desktop_environment:
            return self.__desktop_environment

    def get_window_manager(self):
        if self.__window_manager:
            return self.__window_manager

    def get_deb_packages(self):
        if self.__deb_packages:
            return self.__deb_packages

    def get_flatpak_packages(self):
        if self.__flatpak_packages:
            return self.__flatpak_packages

    def get_snap_packages(self):
        if self.__snap_packages:
            return self.__snap_packages

    def get_font(self):
        if self.__font:
            return self.__font

    def get_browser(self):
        if self.__browser:
            return self.__browser


if __name__ == '__main__':
    oi = OsInfo()
    test = 1
    if test == 0:
        r = oi.get_all_release_info()
        for k, v in r.items():
            print(k + ':', v)
    else:
        print('    current-user:', oi.get_current_user())
        print('current-username:', oi.get_current_username())
        print('        hostname:', oi.get_hostname())
        print('     pretty-name:', oi.get_pretty_name())
        print('            name:', oi.get_name())
        print('         name-id:', oi.get_name_id())
        print('        codename:', oi.get_codename())
        print('         version:', oi.get_version())
        print('          kernel:', oi.get_kernel())
        print('  kernel-version:', oi.get_kernel_version())
        print('    architecture:', oi.get_architecture())
