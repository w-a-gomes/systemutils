#!/usr/bin/env python3
# https://github.com/w-a-gomes/osutility
import re
import subprocess
import threading
from urllib.parse import unquote


class File(object):
    """Create an object of type 'File'

    Extract information from a file, including "slice" the URL.
    """

    def __init__(self, file_url):
        """Class constructor"""
        self.__file_url = file_url
        self.__file = None
        self.__path = None
        self.__name = None
        self.__extension = None
        self.__mime = None
        self.__size = None

    # __Getters___
    def get_file(self) -> str:
        """Gets the complete URL of the file

        Returns a clean URL, with no prefixes like "file://" and "UrlEncode" formatting.

        :return: String containing the URL.
        """
        if self.__file:
            return self.__file

        self.__file = self.__extract_file(self.__file_url)
        return self.__file

    def get_path(self) -> str:
        """Get the file path

        Only the working path of the file, without its name and extension.

        :return: String containing the working URL of the file
        """
        if self.__path:
            return self.__path

        if not self.__file:
            self.__file = self.__extract_file(self.__file_url)
        self.__path = self.__extract_path(self.__file)
        return self.__path

    def get_name(self) -> str:
        """Get the file name

        Only the clean name, without the working path or file extension.

        :return: String containing the file name
        """
        if self.__name:
            return self.__name

        if not self.__file:
            self.__file = self.__extract_file(self.__file_url)

        self.__name = self.__extract_name(self.__file)
        return self.__name

    def get_extension(self) -> str:
        """Get the file extension

        Only the file extension without your name.

        :return: String containing the file extension
        """
        if self.__extension:
            return self.__extension

        if not self.__file:
            self.__file = self.__extract_file(self.__file_url)

        self.__extension = self.__extract_extension(self.__file)
        return self.__extension

    def get_mime(self) -> str:
        """Get the file's mime type

        The mime type is used to identify the file in the association of programs and icons.

        :return: String containing the file's mime type
        """
        if self.__mime:
            return self.__mime

        if not self.__file:
            self.__file = self.__extract_file(self.__file_url)

        self.__mime = self.__extract_mime(self.__file)
        return self.__mime

    def get_size(self) -> str:
        """Get the file size

        The calculation to determine the file size can take time depending on the file, so
        this value is disabled by default. Use "set_enable_size()" to enable.
        For directories, the value obtained is the number of items.

        :return: String containing the file size
        """
        if self.__size:
            return self.__size

        if not self.__file:
            self.__file = self.__extract_file(self.__file_url)

        self.__size = 'calculating'
        self.__extract_size(self.__file)
        return self.__size

    # ___Setters___
    def set_file(self, arg: str) -> str:
        """Configure a new string for this object/file

        Example: "/home/user/new_file.txt"

        :param arg: String containing a file URL
        :return: String containing the passed value
        """
        if subprocess.getoutput('test -f "{}" && echo $?'.format(arg)) != '0':
            print('Warning! File not found.\nTip: Pass an absolute path.')

        self.__file_url = arg
        self.__file = self.__extract_file(self.__file_url)
        if self.__path:
            self.__path = self.__extract_path(self.__file)
        if self.__name:
            self.__name = self.__extract_name(self.__file)
        if self.__extension:
            self.__extension = self.__extract_extension(self.__file)
        if self.__mime:
            self.__mime = self.__extract_mime(self.__file)
        self.__size = None

        return self.__file

    def set_path(self, arg: str) -> str:
        """Set up a new working path at the URL of this object/file

        Example: "/home/user/foo/"

        :param arg: String with the new working path of the file
        :return: String containing the passed value
        """
        # Verifica a barra do path
        if arg[-1] != '/':
            arg += '/'

        # Avisa se é um path válido
        path = arg
        if subprocess.getoutput('test -d "{}" && echo $?'.format(path)) != '0':
            print('Warning! Path not found.\nTip: Pass an absolute path.')

        # Atualiza caminho original
        name = self.get_name()
        ext = self.get_extension()
        self.__file_url = path + name + ext

        # Atualiza arquivo
        if self.__file:
            self.__file = self.__file_url

        # Atualiza o path
        self.__path = path

        self.__size = None
        return self.__path

    def set_name(self, arg: str) -> str:
        """Set a new name for this object/file

        If you have a file called "foo" like "/home/user/foo.txt", and want to
        rename it to "bar" like "/home/user/bar.txt", simply pass a string like "bar".

        :param arg: String with the new file name
        :return: String containing the passed value
        """
        # Atualiza caminho original
        path = self.get_path()
        name = arg
        ext = self.get_extension()
        self.__file_url = path + name + ext
        self.__file = self.__file_url

        # Atualiza nome
        self.__name = arg

        return self.__name

    def set_extension(self, arg: str) -> str:
        """Set a new extension for this object/file

        :param arg: String with the new extension
        :return: String containing the passed value
        """
        extension = arg
        if extension != '' and extension[0] != '.':
            extension = '.' + arg

        # Atualiza caminho original e o arquivo.
        # Pode haver palavras iguais ao nome da extensão no corpo do texto,
        # por isso, primeiro remove a extensão original somente do final do nome,
        # depois insere a nova extensão no fim.
        self.__file = self.__file[:-len(self.__extension)] + extension
        self.__file_url = self.__file

        # Atualiza extensão
        self.__extension = extension

        # Atualiza mime
        if self.__mime:
            self.__mime = self.__extract_mime(self.__file)
        self.__size = None

        return self.__extension

    def set_mime(self, arg: str) -> str:
        """Set a new mime type for this object/file

        The mime type is used to identify the file in the association of programs and icons.
        Some examples of mime types:
            application/zip;
            image/svg+xml;
            image/x-xcf;
            inode/directory;
            text/html;
            text/plain;
            text/x-python;
            text/x-python3;
            video/mp4;

        :param arg: String with the new new mime type
        :return: String containing the passed value
        """
        self.__mime = arg
        return self.__mime

    # __private__
    @staticmethod
    def __clear_url(arg: str) -> str:
        # Limpa a url dos arquivos
        #
        # file:// /home/user/file
        # file:/  /home/user/file
        # file:   /home/user/file
        # file    /home/user/file
        # //      /home/user/file
        # /       /home/user/file
        #         /home/user/file

        regex = re.findall(r'(file://|file:/|file:|file|//|/|)/.+', arg)
        if regex:
            clean_file = unquote(arg.replace(regex[0], ''))
        else:
            clean_file = unquote(arg)

        return clean_file

    def __extract_file(self, arg: str) -> str:
        return self.__clear_url(arg)

    @staticmethod
    def __extract_path(arg: str) -> str:
        # Extrai somente o caminho do arquivo
        regex = re.findall(r'/.+/', arg)
        if regex:
            return regex[0]

        return ''

    def __extract_name(self, arg: str) -> str:
        # Extrai somente o nome do arquivo
        # sem a extensão ou o caminho dele
        path = self.__extract_path(arg)
        extension = self.__extract_extension(arg)
        return arg.replace(path, '').replace(extension, '')

    @staticmethod
    def __extract_extension(arg: str) -> str:
        # Extrai somente a extensão do arquivo
        # import os
        # >>> filename, file_extension = os.path.splitext("/home/user/Documentos/Documentos.tar.gz")
        # >>> filename
        # '/home/user/Documentos/Documentos.tar'
        # >>> file_extension
        # '.gz'

        file_name = arg

        if file_name[0] == '.':  # Remover ponto inicial para não afetar a posterior divisão e...
            file_name = file_name.lstrip('.')  # ...comparação. Nada é alterado na extensão.

        if '.' not in file_name:  # Arquivo sem extensão
            extension = ''

        elif file_name[-1] == '.':  # Um '.' no fim, faz parte do NOME e pode ser renomeado, i.e, não precisa...
            extension = ''  # ...ser retirado pois não é uma extensão

        else:
            separate_at_dots = file_name.split('.')

            # Lista sempre de 2 itens. Arquivo só tem uma extensão, ou um ponto
            if len(separate_at_dots) == 2:
                extension = '.' + separate_at_dots[-1]

            # Lista sempre de 3 itens pra cima. Arquivo tem mais de uma extensão, ou pontos no meio do nome
            else:
                # Verifica extensão internas (penúltimo item). Adicionar futuramente, extensões internas aqui
                if separate_at_dots[-2] == 'tar':
                    extension = '.' + separate_at_dots[-2] + '.' + separate_at_dots[-1]

                # Não havendo mais, a última parte é sempre uma extensão, vide a falta delas ser tratadas no topo
                else:
                    extension = '.' + separate_at_dots[-1]

        return extension

    def __extract_mime(self, arg: str) -> str:
        # Extrai o tipo mime do arquivo
        mime = self.__hack__mime(arg)
        if mime == 'text/plain;':
            sub = subprocess.getoutput('file --mime --dereference "{}"'.format(arg))
            regex = re.findall(r'^.*: (.+;).+', sub)
            if regex:
                return regex[0]

        return mime

    @staticmethod
    def __hack__mime(arg):
        # Força a criação de tipos mimes para determinadas extensões
        mime = 'text/plain;'
        hack_extensions_filter = {
            '.py': 'text/x-python;',
            '.apk': 'application/vnd.android.package-archive;',
            '.md': 'text/markdown;',
            '.oxt': 'application/vnd.openofficeorg.extension;',
            '.mp3': 'audio/mpeg;'
        }
        for key, value in hack_extensions_filter.items():
            if arg[-len(key):] == key:
                mime = value

        return mime

    def __extract_size(self, arg: str):
        # Inicia uma thread para calcular o tamanho do arquivo em background
        thread = threading.Thread(target=self.__extract_size_threading, args=[arg])
        thread.daemon = True
        thread.start()

    def __extract_size_threading(self, arg: str):
        # Método na thread que calcula o tamanho do arquivo e o retorna
        if not self.__mime:
            if not self.__file:
                self.__file = self.__extract_file(self.__file_url)
            self.__mime = self.__extract_mime(self.__file)

        if self.__mime == 'inode/directory;':
            size = str(int(subprocess.getoutput('ls -l "{}" | wc -l'.format(arg))) - 1)
        else:
            awk = "awk '{print $1}'"
            size = subprocess.getoutput('du -h --summarize --dereference "{}" | {}'.format(arg, awk))
        self.__size = size


if __name__ == '__main__':
    import time
    f = File(__file__)
    f.get_size()
    time.sleep(0.1)
    print(f.__dict__)
    print('     file:', f.get_file())
    print('     name:', f.get_name())
    print('     path:', f.get_path())
    print('extension:', f.get_extension())
    print('     size:', f.get_size())
    print('     mime:', f.get_mime())
