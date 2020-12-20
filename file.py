#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils
import re
import os
from urllib.parse import unquote

import pathlib

import magic  # python3-magic


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class LengthError(Error):
    """Very long name

    Name greater than 255 characters (the extension is included in the sum)
    """
    def __init__(self, message):
        print(message)


class CharacterError(Error):
    """Characters not allowed.

    Exception raised when characters that are not allowed in filenames are encountered.
    The forward slash (/) is an example.
    """
    def __init__(self, message):
        print(message)


class ExistingNameError(Error):
    """Existing name

    Exception raised when the file name already matches an existing file name in the directory.
    """
    def __init__(self, message):
        print(message)


class File(object):
    """Create an object of type 'File'

    Extract information from a file, including "slice" the URL.
    """

    def __init__(self, file_url: str):
        """Class constructor"""
        self.__url = self.__resolve_url(file_url)      # Uses:
        self.__url_history = [self.__url]              # url
        self.__mime = self.__resolve_mime()            # url
        self.__path = self.__resolve_path()            # url
        self.__extension = self.__resolve_extension()  # mime, url, path
        self.__name = self.__resolve_name()            # url, path, extension
        self.__is_link = self.__resolve_is_link()      # url

    def get_url(self) -> str:
        """File URL

        Get the updated file url and cleanly.

        ›››file = File('/home/user/user name.txt')
        ›››file.get_url()
        /home/user/user name.txt

        :return: URL
        """
        return self.__url

    @staticmethod
    def __resolve_url(arg: str) -> str:
        # Limpa a url dos arquivos
        regex = re.findall(r'(file://|file:/|file:|file|//|/|)/.+', arg)
        if regex:
            clean_file = unquote(arg.replace(regex[0], ''))
        else:
            clean_file = unquote(arg)

        if not os.path.isfile(clean_file):
            raise FileNotFoundError('The file in the past url does not exist', clean_file)

        return clean_file

    def get_path(self) -> str:
        """Get the file path

        Only the working path of the file, without its name and extension.

        ›››file = File('/home/user/user name.txt')
        ›››file.get_path()
        /home/user/

        :return: String containing the working URL of the file
        """
        return self.__path

    def __resolve_path(self) -> str:
        regex = re.findall(r'/.+/', self.__url)
        path = regex[0]
        return path

    def get_name(self) -> str:
        """Get the file name

        Only the clean name, without the working path or file extension.

        ›››file = File('/home/user/user name.txt')
        ›››file.get_name()
        user name

        :return: String containing the file name
        """
        return self.__name

    def __resolve_name(self) -> str:
        name = self.__url.replace(self.get_path(), '').replace(self.get_extension(), '')
        return name

    def get_extension(self) -> str:
        """Get the file extension

        Only the file extension without your name.

        ›››file = File('/home/user/user name.txt')
        ›››file.get_extension()
        .txt

        :return: String containing the file extension
        """
        return self.__extension

    def __resolve_extension(self) -> str:
        # Extrai somente a extensão do arquivo

        # >>> filename, file_extension = os.path.splitext("/home/user/Documentos/Documentos.tar.gz")
        # >>> filename
        # '/home/user/Documentos/Documentos.tar'
        # >>> file_extension
        # '.gz'

        file_name = self.__url.replace(self.get_path(), '')

        # Remove ponto no início do nome do arquivo para não afetar a
        # posterior divisão e comparação. Nada é alterado na extensão.
        if file_name[0] == '.':
            file_name = file_name.lstrip('.')

        # Arquivos sem extensão
        condition = [
            # Sem extensão.
            '.' not in file_name,

            # Arquivo terminado com um ponto, é também um arquivo sem extensão, pois um ponto (.) no fim
            # faz parte do nome e pode ser renomeado, i.e, não precisa ser retirado pois não é uma extensão.
            file_name[-1] == '.',

            # "Arquivos" que são na realidade diretórios, logicamente não retornam extensão.
            self.get_mime() == 'inode/directory'
        ]
        if any(condition):
            return ''

        # Divide o nome do arquivo em todos os pontos, criando uma lista.
        # O último ou últimos items, representam a extensão. Será verificado abaixo.
        separate_at_dots = file_name.split('.')

        # Uma lista de 2 itens, representa um arquivo que só tem uma extensão, visto
        # que anomalias com pontos no início e fim ja foram tratados.
        # O primeiro item é o nome do arquivo, e último item é a extensão.
        if len(separate_at_dots) == 2:
            return '.' + separate_at_dots[-1]

        # Lista sempre de 3 itens pra cima, representa arquivo que tem mais de uma extensão,
        # ou pontos no meio do nome.
        # Verifica extensão interna (penúltimo item). Adicionar futuramente, extensões internas aqui.
        if separate_at_dots[-2] == 'tar':
            extension = '.' + separate_at_dots[-2] + '.' + separate_at_dots[-1]

        # Não havendo mais "tratamento", a última parte é sempre uma extensão.
        else:
            extension = '.' + separate_at_dots[-1]

        return extension

    def get_mime(self) -> str:
        """Get the file's mime type

        The mime type is used to identify the file in the association of programs and icons.

        ›››file = File('/home/user/user name.txt')
        ›››file.get_mime()
        text/plain

        :return: String containing the file's mime type
        """
        return self.__mime

    def __resolve_mime(self) -> str:
        # Força a criação de tipos mimes para determinadas extensões
        mime = 'text/plain'
        hack_extensions_filter = {
            '.svg': 'image/svg+xml',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.py': 'text/x-python',
            '.md': 'text/markdown',
            '.oxt': 'application/vnd.openofficeorg.extension',
            '.mp3': 'audio/mpeg',
            '.apk': 'application/vnd.android.package-archive',
        }
        for key, value in hack_extensions_filter.items():
            if self.__url[-len(key):].lower() == key:
                mime = value

        if mime == 'text/plain':
            magic_mime = magic.Magic(mime=True)
            try:
                mime = magic_mime.from_buffer(open('{}'.format(self.__url), 'rb').read(2048))
            except IsADirectoryError:
                mime = 'inode/directory'

        return mime

    def get_is_link(self) -> bool:
        """Checks whether a file is a link

        ›››file = File('/home/user/user name.txt')
        ›››file.get_is_link()
        False

        :return: True or False
        """
        return self.__is_link

    def __resolve_is_link(self) -> bool:
        return os.path.islink(self.__url)

    def get_url_history(self) -> list:
        """List with URL that has already been modified

        When a file name is changed, it is saved in a history for later comparison.

        ›››file = File('/home/user/user name.txt')
        ›››file.get_url_history()
        ['/home/user/user name.txt']
        ›››file.set_name('foo')
        ›››file.get_url()
        /home/user/foo.txt
        ›››file.set_name('bar')
        ›››file.get_url()
        /home/user/bar.txt
        ›››file.get_url_history()
        ['/home/user/user name.txt', '/home/user/foo.txt', '/home/user/bar.txt']

        :return: List with URL
        """
        return self.__url_history

    def set_name(self, name: str) -> None:
        """Sets a new name for the file

        If the name passed cannot be used for any reason, an exception is raised.

        Exceptions:
          LengthError: Name greater than 255 characters (the extension is included in the sum)
          CharacterError: Characters not allowed, such as the slash
          ExistingNameError: Name that already exists in some file in the directory

        ›››file = File('/home/user/user name.txt')
        ›››file.get_name()
        user name
        ›››file.set_name('foobar')
        ›››file.get_name()
        foobar
        ›››file.get_url()
        /home/user/foobar.txt

        :param name: New name for the file
        """
        extension = self.get_extension()

        # Errors
        if len(name) + len(extension) > 255:
            raise LengthError(message='File name longer than 255 characters (including extension)')
        if '/' in name:
            raise CharacterError(message='Names cannot contain the / (slash) character')
        if name != self.get_name():
            if name + extension in os.listdir(self.get_path()):
                raise ExistingNameError(
                    message='A file with that name "{}" already exists in the directory'.format(name + extension)
                )

        # Updates
        self.__url = self.get_path() + name + extension
        self.__url_history.append(self.__url)
        self.__name = name

    def set_path(self, path: str) -> None:
        """"""

        path = path + '/' if path[-1] != '/' else path
        name = self.get_name()
        extension = self.get_extension()

        # Erro: Caminho existe
        if not os.path.isdir(path):
            raise NotADirectoryError('The path in the url "{}" does not exist'.format(path))

        # Erro: ESTE "arquivo/nome de arquivo" já existe no caminho passado
        if name + extension in os.listdir(path):
            raise ExistingNameError(
                message='In the provided path, there is already a file with the same'
                        'name as this object ({})'.format(name + extension)
            )

        # Updates
        self.__url = path + name + extension
        self.__url_history.append(self.__url)
        self.__path = path


if __name__ == '__main__':
    f = File(file_url=os.path.dirname(os.path.abspath(__file__)) + '/file.py')
    print('      url:', f.get_url())
    print('     path:', f.get_path())
    print('     name:', f.get_name())
    print('extension:', f.get_extension())
    print('     mime:', f.get_mime())
    print('     link:', f.get_is_link())
    print()
    try:
        f.set_name('test')
    except LengthError as error:
        print(error)
    except CharacterError as error:
        print(error)
    except ExistingNameError as error:
        print(error)
    print()
    print('      url:', f.get_url())
    print('     path:', f.get_path())
    print('     name:', f.get_name())
    print('extension:', f.get_extension())
    print('     mime:', f.get_mime())
    print('     link:', f.get_is_link())
    print()
    try:
        f.set_path(path=os.path.dirname(os.path.abspath(__file__)) + '/test/')
    except NotADirectoryError as error:
        print(error)
    except ExistingNameError as error:
        print(error)
    print()
    print('      url:', f.get_url())
    print('     path:', f.get_path())
    print('     name:', f.get_name())
    print('extension:', f.get_extension())
    print('     mime:', f.get_mime())
    print('     link:', f.get_is_link())
    print()
    print('history:')
    for item in f.get_url_history():
        print(item)
