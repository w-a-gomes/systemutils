#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils
import os

import file


class ListFiles(object):
    """Create an object of type 'ListFiles'

    List of files in the directory.
    """
    def __init__(self, path: str = None):
        """Class constructor"""
        super().__init__()
        self.__path = path
        self.__list_files = list()

    def get_list(self):
        """List of files in the directory

        Returns a list of objects of type 'File'. The 'File' type objects
        have methods that show information about the listed file.

        :return: List of objects of type 'File'
        """
        if self.__list_files:
            return self.__list_files

        self.__create_list()
        return self.__list_files

    def __create_list(self):
        # Cria a lista com items listados no diretório
        ls_items = self.__ls_items()
        for item in ls_items:
            file_item = file.File(item)
            self.__list_files.append(file_item)

    def __ls_items(self):
        # Lista os itens no diretório
        if self.__path[-1] != '/':
            self.__path += '/'

        ls_path = os.listdir()
        ls_items = list()
        for item in ls_path:
            ls_items.append(self.__path + item)

        return ls_items


if __name__ == '__main__':
    files = ListFiles(os.path.dirname(os.path.abspath(__file__)))
    list_files = files.get_list()
    n = 25
    prefix = ' ' * n
    print(('FILE' + prefix)[:n] + ('EXTENSION' + prefix)[:n])
    for f in list_files:
        print(
            (f.get_name() + f.get_extension() + prefix)[:n] +
            '|' + (f.get_extension() + prefix)[:n]
        )
