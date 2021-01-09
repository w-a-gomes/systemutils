#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils
import os
from urllib.parse import unquote


class File(object):
    """Create an object of type 'File'

    Extract information from a file, including "slice" the URL.
    """

    def __init__(self, file_url: str, use_extensions_list: list = None):
        """Class constructor"""
        self.extensions_list = use_extensions_list
        self.__url = self.__resolve_url(file_url)  # isdir
        self.__url_history = [self.__url]
        self.__path = self.__resolve_path()
        self.__extension = self.__resolve_extension()  # isdir, path
        self.__name = self.__resolve_name()  # path, extension

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
        url_file = unquote(arg.replace('file://', ''))

        # Garantir que url sempre comece com apenas uma barra,
        # porque a validação da url com os.path() não levanta erro
        # em url com várias barras
        if '//' in url_file:
            while '//' in url_file:
                url_file = url_file.replace('//', '/')

        return url_file

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
        return os.path.dirname(self.__url) + '/'

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

        # splitext não funciona para .tar*
        # >>> filename, file_extension = os.path.splitext("/home/user/Documentos/Documentos.tar.gz")
        # >>> file_extension
        # '.gz'

        # Remover o ponto '.' no início do nome do arquivo para não afetar a
        # posterior divisão e comparação. Nada é alterado na extensão.
        # O motivo deste tipo de validação, é que simplesmente "olhar" para
        # o fim do nome do arquivo a partir do último ponto, não produz o
        # resultado esperado, pois um arquivo de nome '.txt' não pode ser
        # reconhecido como um arquivo de nome vazio '' e extensão '.txt'
        file_name = self.__url.replace(self.get_path(), '').lstrip('.')

        # Arquivos sem extensão
        condition = [
            # Sem extensão.
            # Pontos '.' no início do nome do arquivo ja foram removidos
            # para esta comparação.
            '.' not in file_name,

            # Arquivo terminado com um ponto, é também um arquivo sem extensão,
            # pois um ponto '.' no fim, faz parte do nome e pode ser renomeado,
            # i.e, não precisa ser retirado pois não é uma extensão.
            file_name[-1] == '.',
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
            ext = '.' + separate_at_dots[-1]

            # Verifica se a extensão existe em uma lista de extensões
            if self.extensions_list:
                if ext in self.extensions_list:
                    return ext
                else:
                    return ''
            return ext

        # Lista sempre de 3 itens pra cima, representa arquivo que
        # tem mais de uma extensão, ou pontos no meio do nome.
        # Será verificado extensões internas (penúltimo item, como 'tar').
        # Futuramente, adicionar extensões internas aqui.
        if len(separate_at_dots) > 2:
            ext = '.' + separate_at_dots[-1]

            # Se existe extensão interna
            if separate_at_dots[-2] == 'tar':
                ext = '.' + separate_at_dots[-2] + ext

            # Verifica se a extensão existe em uma lista de extensões
            if self.extensions_list:
                if ext in self.extensions_list:
                    return ext
                else:
                    return ''

            return ext

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
          CharacterError: Characters not allowed, such as the slash (/)
          ExistingNameError: Name that already exists in some file in the directory
          NameNotAllowedError: 

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
        self.__url = self.get_path() + name + extension
        self.__url_history.append(self.__url)
        self.__name = name


class ValidateFile(object):
    def __init__(self, file: File):
        self.__file = file
        self.__error = dict()
        self.__is_valid_file = self.__validate_file()

    def is_valid_file(self) -> bool:
        return self.__is_valid_file

    def get_error(self) -> dict:
        return self.__error

    def __validate_file(self) -> bool:
        path = self.__file.get_path()
        name = self.__file.get_name()
        extension = self.__file.get_extension()

        if '/' in name:
            msg = 'Names cannot contain the / (slash) character'
            self.__error['character-error'] = msg
        if name + extension == '.' or name + extension == '..':
            msg = 'It is not possible to use one dot (.) or two dots (..) as a filename'
            self.__error['name-not-allowed-error'] = msg
        if name + extension in os.listdir(path):
            msg = 'A file with that name already exists in the directory'
            self.__error['existing-name-error'] = msg
        if len(name + extension) > 255:
            msg = 'Filename longer than 255 characters (including extension)'
            self.__error['length-error'] = msg
        if name[0] == '.' and name + extension != '.' and name + extension != '..':
            msg = 'Files that start with a dot (.) will be hidden'
            self.__error['hidden-file-error'] = msg

        return True if not self.__error else False


if __name__ == '__main__':
    f = File(file_url=os.path.abspath(__file__))
    is_dir = os.path.isdir(f.get_url())
    print('      url:', f.get_url())
    print('     path:', f.get_path())
    print('     name:', f.get_name())
    print('extension:', '' if is_dir else f.get_extension())
    print('   is dir:', is_dir)
    print('  is link:', os.path.islink(f.get_url()))
    print()
    f.set_name('.foo')
    v = ValidateFile(f)
    if not v.is_valid_file():
        for item_error, message in v.get_error().items():
            print(message)
    print()
    print('     name:', f.get_name())
    print('      url:', f.get_url())
    print()
    print('history:')
    for item in f.get_url_history():
        print(item)
