import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def load_file(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        return f.read()


setup(
    version='1.2',
    author='Joakim Saario',
    author_email='saario.joakim@gmail.com',
    name='try_default',
    packages=['try_default'],
    install_requires=['six'],
    description='A microlibrary for handling exceptions',
    long_description=load_file('README.rst'),
    url='https://github.com/jocke-l/try-default',
    license='3-Clause BSD License',
    keywords=['util', 'functional', 'exceptions', 'microlibrary'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers'
    ]
)
