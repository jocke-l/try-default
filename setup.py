try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import try_default

setup(
    version=try_default.__version__,
    author='Joakim Saario',
    author_email='joakim@5monkeys.se',
    name='try_default',
    py_modules=['try_default'],
    description='A microlibrary for handling exceptions',
    keywords=['util', 'functional', 'exceptions', 'micro-library'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License'
    ]
)
