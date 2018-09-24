import inspect

import six

getargspec = inspect.getargspec if six.PY2 else inspect.getfullargspec
