import functools
import inspect

import six

from . import _compat
from ._utils import curried

__all__ = ['try_default']


@curried
def try_default(expr, default):
    """
    Function variant of try-except clause with default value on
    exception.

    Allows inline replacement for cases such as:

    .. code-block:: python

        empty_list = []

        try:
            foo = empty_list[1]
        except IndexError:
            foo = 0

    It is also possible to pass arguments ``expr`` like so:

    .. code-block:: python

        handle = try_default(lambda a: a[0], {IndexError: 0})

        handle([])
        # returns 0

        handle([1])
        # returns 1

    Decorators are also supported:

    .. code-block:: python

        @try_default({IndexError: 0})
        def handle(a):
            return a[0]


        handle([])
        # returns 0

        handle([1])
        # returns 1

    If the raised exception is not in ``default``, it will be
    re-raised.

    :param expr: Intended to be a lazy expression, implemented as a function.
    :type expr: Callable[..., Any]
    :param default: Example: ``{IndexError: 0}``
    :type default: Mapping[BaseException, Any]
    :return: Result of calling ``expr``. On exception this will
             be the specified default value.
    """

    if not six.callable(expr):
        # Flip arguments. We were most likely invoked with a decorator.
        expr, default = default, expr

    @functools.wraps(expr)
    def act(*args, **kwargs):
        inspect.getcallargs(expr, *args, **kwargs)

        try:
            return expr(*args, **kwargs)
        except BaseException as e:
            # This can't easily be achieved using `__getitem__` without
            # breaking any exception hierarchies. That's why we're
            # looping over `default` instead. That way, we can have
            # Python do the hard OOP work by using `isinstance`.
            for key, value in six.iteritems(default):
                if isinstance(e, key):
                    return value

            # Re-raise unhandled exceptions.
            raise

    return act if any(_compat.getargspec(expr)) else act()
