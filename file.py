#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils
import re
import os.path

import magic  # python3-magic
from urllib.parse import unquote


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class LengthError(Error):
    def __init__(self, message):
        self.message = message


class CharacterError(Error):
    def __init__(self, message):
        self.message = message


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

    def get_url(self):
        return self.__url

    @staticmethod
    def __resolve_url(arg: str) -> str:
        # Limpa a url dos arquivos
        regex = re.findall(r'(file://|file:/|file:|file|//|/|)/.+', arg)
        if regex:
            clean_file = unquote(arg.replace(regex[0], ''))
        else:
            clean_file = unquote(arg)

        return clean_file

    def get_path(self) -> str:
        """Get the file path

        Only the working path of the file, without its name and extension.

        :return: String containing the working URL of the file
        """
        return self.__path

    def __resolve_path(self):
        regex = re.findall(r'/.+/', self.__url)
        path = regex[0]
        return path

    def get_name(self) -> str:
        """Get the file name

        Only the clean name, without the working path or file extension.

        :return: String containing the file name
        """
        return self.__name

    def __resolve_name(self):
        name = self.__url.replace(self.get_path(), '').replace(self.get_extension(), '')
        return name

    def get_extension(self) -> str:
        """Get the file extension

        Only the file extension without your name.

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

        :return: String containing the file's mime type
        """
        return self.__mime

    def __resolve_mime(self):

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
        return self.__is_link

    def __resolve_is_link(self) -> bool:
        return os.path.islink(self.__url)

    def get_url_history(self):
        return self.__url_history

    def set_name(self, name: str) -> None:
        extension = self.get_extension()
        if len(name) + len(extension) > 255:
            raise LengthError(message='File name longer than 255 characters (including extension)')
        if '/' in name:
            raise CharacterError(message='Names cannot contain the / (slash) character')

        self.__url = self.get_path() + name + extension
        self.__url_history.append(self.__url)
        self.__name = name


if __name__ == '__main__':
    f = File(file_url=os.path.dirname(os.path.abspath(__file__)) + '/' + __file__)
    print('      url:', f.get_url())
    print('     path:', f.get_path())
    print('     name:', f.get_name())
    print('extension:', f.get_extension())
    print('     mime:', f.get_mime())
    print('     link:', f.get_is_link())
    print()
    try:
        f.set_name('foo')
    except LengthError as error:
        print(error.message)
    except CharacterError as error:
        print(error.message)
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
