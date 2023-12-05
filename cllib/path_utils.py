import os
import tempfile
from pathlib import Path
from typing import TypeVar

PathStr = TypeVar("PathStr", str, Path)  # type of str or Path


def rel2abs(src, *paths):
    """  Output is absolute path of paths joined with src's dir

    Example:
    >>> rel2abs('/opt/aaa/abc.xml', 'corrections.csv')
    '/opt/aaa/corrections.csv'
    >>> rel2abs('/opt/aaa/', 'corrections.csv')
    '/opt/aaa/corrections.csv'
    >>> rel2abs('/opt/aaa/abc.xml', '..', 'corrections.csv')
    '/opt/corrections.csv'

    :param src:
    :param paths:
    :return:
    """
    src = os.path.realpath(src)
    if os.path.isfile(src):
        src = os.path.dirname(src)
    return os.path.abspath(os.path.join(src, *paths))


def list_subdirs(path):
    return [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]


def abs_dir_path(src: PathStr) -> str:
    """ Return absolute dir path of src

    Example:
    >>> abs_dir_path('/opt/aaa/abc.xml')
    '/opt/aaa'
    >>> abs_dir_path('/opt/aaa/')
    '/opt'
    """
    return os.path.dirname(os.path.realpath(src))


def create_tmp_path(*args, **kwargs):
    for _ in range(1000):
        file = tempfile.NamedTemporaryFile(*args, **kwargs)
        file.close()  # close to remove file
        if os.path.exists(file.name):
            continue
        else:
            return file.name
    raise FileExistsError('can\' create tmp file, file already exist')


def create_tmp_dir(*args, is_auto_mkdir=False, num_retry=20, **kwargs) -> Path:
    path = Path(create_tmp_path(*args, **kwargs))
    if is_auto_mkdir:
        path.mkdir(parents=True, exist_ok=True)
    return path
