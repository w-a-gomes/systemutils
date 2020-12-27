#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils
import subprocess
import disk


class ListDisks(object):
    """Create an object of type 'ListDisks'

    List of system disks.
    """
    def __init__(self):
        """Class constructor"""
        self.__list = list()

    def get_list(self) -> list:
        """List of system disks

        Returns a list of objects of type 'Disk'. Objects of type 'Disk'
        have methods that show information about the listed disk.

        :return: List of objects of type 'Disk'
        """
        if not self.__list:
            self.__list = self.__create_list()

        return self.__list

    def __create_list(self) -> list:
        # Cria a lista dos discos listados
        ls_items = self.__ls_items()
        list_items = list()

        for item in ls_items:
            item_disk = disk.Disk(item)
            list_items.append(item_disk)

        return list_items

    @staticmethod
    def __ls_items():
        # lista os discos do sistema
        ls_info = subprocess.getoutput('df -hT').split('\n')
        del (ls_info[0])
        ls_disk = list()
        for item in ls_info:
            info_item = item.split()
            # Pegar somente itens que forem discos montáveis
            if info_item[0][:1] == '/':
                ls_disk.append(info_item[0])
        return ls_disk


if __name__ == '__main__':
    d = ListDisks()
    d_list = d.get_list()
    for disk_item in d_list:
        if 'loop' not in disk_item.get_system_file_name():
            print(disk_item.get_system_file_name() + ':', disk_item.get_disk_identify())
