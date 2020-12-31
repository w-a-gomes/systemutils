import pytest
import file
import os


@pytest.fixture
def readme():
    path = os.path.abspath(__file__).replace('files/test_file.py', 'README.md')
    return file.File(file_url=path)


def test_readme_name(readme):
    assert readme.get_name() == 'README'


def test_readme_extension(readme):
    assert readme.get_extension() == '.md'


def test_readme_is_dir(readme):
    assert not readme.is_directory()


@pytest.fixture
def licenses():
    path = os.path.abspath(__file__).replace('files/test_file.py', 'LICENSE')
    return file.File(file_url=path)


def test_license_name(licenses):
    assert licenses.get_name() == 'LICENSE'


def test_license_extension(licenses):
    assert licenses.get_extension() == ''


def test_license_is_dir(licenses):
    assert not licenses.is_directory()


@pytest.fixture
def this_dir():
    path = os.path.dirname(os.path.abspath(__file__))
    return file.File(file_url=path)


def test_this_dir_name(this_dir):
    assert this_dir.get_name() == 'files'


def test_this_dir_extension(this_dir):
    assert this_dir.get_extension() == ''


def test_this_dir_is_dir(this_dir):
    assert this_dir.is_directory()


@pytest.fixture
def config():
    path = os.getenv('HOME') + '/.config'
    return file.File(file_url=path)


def test_config_name(config):
    assert config.get_name() == '.config'


def test_config_extension(config):
    assert config.get_extension() == ''


def test_config_is_dir(config):
    assert config.is_directory()


@pytest.fixture
def python3():
    return file.File(file_url='/usr/bin/python3')


def test_python3_url(python3):
    assert python3.get_url() == '/usr/bin/python3'


def test_python3_path(python3):
    assert python3.get_path() == '/usr/bin/'


def test_python3_name(python3):
    assert python3.get_name() == 'python3'


def test_python3_extension(python3):
    assert python3.get_extension() == ''


def test_python3_is_dir(python3):
    assert not python3.is_directory()
