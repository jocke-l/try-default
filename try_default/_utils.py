import functools

from . import _compat


def curried(func):
    if not any(_compat.getargspec(func)):
        return func()

    return functools.update_wrapper(
        lambda *args, **kwargs: curried(
            functools.partial(func, *args, **kwargs)
        ), func
    )
