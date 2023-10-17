import os
import tempfile
from pathlib import Path
from typing import Union, TypeVar

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


def create_tmp_dir(is_auto_mkdir=False, num_retry=20) -> Path:
    for _ in range(num_retry):
        path = Path(tempfile.NamedTemporaryFile().name)
        if not path.exists():
            break
    else:
        raise EnvironmentError(f'create tmp dir retry [{num_retry}] failed')

    if is_auto_mkdir:
        path.mkdir(parents=True, exist_ok=True)
    return path


def abs_dir_path(src: PathStr) -> str:
    """ Return absolute dir path of src

    Example:
    >>> abs_dir_path('/opt/aaa/abc.xml')
    '/opt/aaa'
    >>> abs_dir_path('/opt/aaa/')
    '/opt'
    """
    return os.path.dirname(os.path.realpath(src))
