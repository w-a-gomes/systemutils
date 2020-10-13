#!/usr/bin/env python3
# https://github.com/w-a-gomes/osutility
import subprocess


class Disk(object):
    """Create an object of type 'Disk'

    Extract information from a disk.
    """

    def __init__(self, arg: str):
        """Class constructor"""
        # ID=lsblk: Usam pontos de montagem
        # ID=df: Usam nome do sistema de arquivos

        # -> Todos os ID=df vem abaixo desta linha
        self.__system_file_name = arg
        # -> Todos os ID=lsblk vem abaixo desta linha
        self.__mount_point = self.__df_mount_point(self.__system_file_name)

        self.__parent_kernel_name = None
        self.__kernel_name = None
        self.__system_file_type = None
        self.__partition_type = None
        self.__label = None
        self.__size = None
        self.__used = None
        self.__free = None
        self.__percentage_used = None
        self.__disk_identify = None

    # __Getters__
    def get_system_file_name(self) -> str:
        """Get the file system name

        Filesystem representation of devices your system understands.

        :return: A string with the name of the file system
        """
        return self.__system_file_name

    def get_parent_kernel_name(self) -> str:
        """Get the parent name of the disk kernel name

        Name that the kernel chooses for the main disk in the partitioning hierarchy.

        :return: A string with the relative disk name
        """
        if self.__parent_kernel_name:
            return self.__parent_kernel_name

        self.__parent_kernel_name = self.__lsblk_parent_kernel_name(self.__mount_point)
        return self.__parent_kernel_name

    def get_kernel_name(self) -> str:
        """Get the kernel name of the disk

        Name the kernel chooses for the disk or partition.

        :return: A string with the disk's kernel name
        """
        if self.__kernel_name:
            return self.__kernel_name

        self.__kernel_name = self.__lsblk_kernel_name(self.__mount_point)
        return self.__kernel_name

    def get_mount_point(self) -> str:
        """Get the disk mount point

        Path where the disc was mounted.

        :return: A string with the disk's mount point
        """
        return self.__mount_point

    def get_system_file_type(self) -> str:
        """Get the file system type

        The type of the file system, such as ext4, FAT, NTFS, btrfs...

        :return: A string with the file system type
        """
        if self.__system_file_type:
            return self.__system_file_type

        self.__system_file_type = self.__df_system_file_type(self.__system_file_name)
        return self.__system_file_type

    def get_partition_type(self) -> str:
        """Get the partition type

        Whether it is a partition, the root disk, a disk or virtual partition:
        Partition (part), logical volume (lvm)...

        :return: A string with the partition type
        """
        if self.__partition_type:
            return self.__partition_type

        self.__partition_type = self.__lsblk_partition_type(self.__mount_point)
        return self.__partition_type

    def get_label(self) -> str:
        """Get the disk label

        Disc identification label.

        :return: A string containing the disk label
        """
        if self.__label:
            return self.__label

        self.__label = self.__lsblk_label(self.__mount_point)
        return self.__label

    def get_size(self) -> str:
        """Get the disk size

        Total disk capacity.

        :return: A string with the size of the disk
        """
        if self.__size:
            return self.__size

        self.__size = self.__df_size(self.__system_file_name)
        return self.__size

    def get_used(self) -> str:
        """Get the amount of disk usage

        Disc used quantity.

        :return: A string with the amount of disk usage
        """
        if self.__used:
            return self.__used

        self.__used = self.__df_used(self.__system_file_name)
        return self.__used

    def get_free(self) -> str:
        """Get the free size for disk use

        Remaining disk space.

        :return: A free size string
        """
        if self.__free:
            return self.__free

        self.__free = self.__df_free(self.__system_file_name)
        return self.__free

    def get_percentage_used(self) -> str:
        """Get the size in percent of disk usage

        Disc amount used in percent.

        :return: A string the size in percent of disk usage
        """
        if self.__percentage_used:
            return self.__percentage_used

        self.__percentage_used = self.__df_percentage_used(self.__system_file_name)
        return self.__percentage_used

    def get_disk_identify(self) -> str:
        """Obtain a useful disk ID

        Whether it is a removable, optical, HDD, SSD device ...

        :return: A string with the disk ID
        """
        if self.__disk_identify:
            return self.__disk_identify

        self.__disk_identify = self.__hck_disk_identify(self.__system_file_name)
        return self.__disk_identify

    # __Setters__
    # Nope! :p

    # __private__
    @staticmethod
    def __lsblk_parent_kernel_name(arg: str) -> str:
        p_kernel_nam = subprocess.getoutput('lsblk --list --noheadings -o MOUNTPOINT,PKNAME | grep "{} "'.format(arg))
        return p_kernel_nam.replace(arg, '').strip()

    @staticmethod
    def __lsblk_kernel_name(arg: str) -> str:
        kernel_nam = subprocess.getoutput('lsblk --list --noheadings -o MOUNTPOINT,KNAME | grep "{} "'.format(arg))
        return kernel_nam.replace(arg, '').strip()

    @staticmethod
    def __df_mount_point(arg: str) -> str:
        mount_point = subprocess.getoutput('df -h --output=source,target | grep "{} "'.format(arg))
        return mount_point.replace(arg, '').strip()

    @staticmethod
    def __df_system_file_type(arg: str) -> str:
        sf_type = subprocess.getoutput('df -h --output=source,fstype | grep "{} "'.format(arg))
        return sf_type.replace(arg, '').strip()

    @staticmethod
    def __lsblk_partition_type(arg: str) -> str:
        partition_type = subprocess.getoutput('lsblk --list --noheadings -o MOUNTPOINT,TYPE | grep "{} "'.format(arg))
        return partition_type.replace(arg, '').strip()

    @staticmethod
    def __lsblk_label(arg: str) -> str:
        label = subprocess.getoutput('lsblk --list --noheadings -o MOUNTPOINT,LABEL | grep "{} "'.format(arg))
        return label.replace(arg, '').strip()

    @staticmethod
    def __df_size(arg: str) -> str:
        size = subprocess.getoutput('df -h --output=source,size | grep "{} "'.format(arg))
        return size.replace(arg, '').strip()

    @staticmethod
    def __df_used(arg: str) -> str:
        used = subprocess.getoutput('df -h --output=source,used | grep "{} "'.format(arg))
        return used.replace(arg, '').strip()

    @staticmethod
    def __df_free(arg: str) -> str:
        free = subprocess.getoutput('df -h --output=source,avail | grep "{} "'.format(arg))
        return free.replace(arg, '').strip()

    @staticmethod
    def __df_percentage_used(arg: str) -> str:
        p_used = subprocess.getoutput('df -h --output=source,pcent | grep "{} "'.format(arg))
        return p_used.replace(arg, '').strip()

    @staticmethod
    def __hck_disk_identify(disk_fs: str) -> str:
        # Caminhos que identificam se é um dispositivo óptico
        con = [
            '/dev/cdrom/' in disk_fs,
            '/dev/cdrw/' in disk_fs,
            '/dev/dvd/' in disk_fs,
            '/dev/dvdrw/' in disk_fs,
            '/dev/sr0/' in disk_fs
        ]

        # Comando que identifica se é um dispositivo removível
        removable_cmd = "lsblk --noheadings -o MOUNTPOINT,HOTPLUG " + disk_fs + " | awk '{ print $2 }'"
        return_removable_cmd = subprocess.getoutput(removable_cmd)

        # SSD
        ssd_cmd = "lsblk --noheadings -o MOUNTPOINT,ROTA " + disk_fs + " | awk '{ print $2 }'"
        return_ssd_cmd = subprocess.getoutput(ssd_cmd)

        # Virtual/Loop
        virtual_loop_cmd = "lsblk --noheadings -o MOUNTPOINT,TYPE " + disk_fs + " | awk '{ print $2 }'"
        return_virtual_loop_cmd = subprocess.getoutput(virtual_loop_cmd)

        # Virtual/Drive
        virtual_drive_cmd = "lsblk --noheadings -o MOUNTPOINT,TYPE " + disk_fs + " | awk '{ print $2 }'"
        return_virtual_drive_cmd = subprocess.getoutput(virtual_drive_cmd)

        if any(con):
            device_type = 'optical'
        elif return_removable_cmd == '1':
            device_type = 'removable'
        elif return_ssd_cmd == '0' and return_virtual_loop_cmd != 'loop':
            device_type = 'ssd'
        elif return_virtual_loop_cmd == 'loop':
            device_type = 'virtual-loop'
        elif return_virtual_drive_cmd == 'dm':
            device_type = 'virtual-drive'
        else:
            device_type = 'drive'

        return device_type


if __name__ == '__main__':
    d = Disk("/dev/sda3")
    print('       mount point:', d.get_mount_point())
    print('  system file name:', d.get_system_file_name())
    print('parent kernel name:', d.get_parent_kernel_name())
    print('       kernel name:', d.get_kernel_name())
    print('  system file type:', d.get_system_file_type())
    print('    partition type:', d.get_partition_type())
    print('             label:', d.get_label())
    print('              size:', d.get_size())
    print('              used:', d.get_used())
    print('              free:', d.get_free())
    print('   percentage used:', d.get_percentage_used())
    print('     disk identify:', d.get_disk_identify())
