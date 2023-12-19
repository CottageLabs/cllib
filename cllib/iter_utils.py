import itertools
from typing import Iterable, Any, Callable


class RecordCounter:
    """
    Count iterable items by wrap_iter or __call__

    Examples
    --------
    >>> counter = RecordCounter()
    >>> _ = list(counter.wrap_iter(range(5)))
    >>> counter.cur_size()
    5

    >>> counter = RecordCounter()
    >>> counter('z')
    'z'
    >>> counter.cur_size()
    1
    """

    def __init__(self):
        self._cur_size = 0

    def __call__(self, item):
        self.plus_one()
        return item

    def plus_one(self):
        self._cur_size += 1

    def cur_size(self):
        return self._cur_size

    def wrap_iter(self, items: Iterable):
        return (self(i) for i in items)


def split(values: Iterable, cond_fn: Callable[[Any], bool]):
    a, b = itertools.tee(values)
    return (i for i in a if cond_fn(i)), (i for i in b if not cond_fn(i))
