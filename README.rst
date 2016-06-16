try-default
===========

A microlibrary for handling exceptions.

Example:

.. code-block:: python

    from try_default import try_default

    baz = []
    result = try_default(lambda: baz[0], {IndexError: 'n/a'})
    # result: 'n/a'

    baz = ['spam']
    result = try_default(lambda: baz[0], {IndexError: 'n/a'})
    # result: 'spam'

    result = try_default(lambda: {'egg': baz[0]}['spam'],
                         {IndexIError: 'n/a/'})
    # Raises KeyError
