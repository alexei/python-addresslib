# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='python-addresslib',
    packages=['addresslib'],
    version='1.0.3',
    description='Python email address parsing library',
    author='Alexei',
    author_email='hello@alexei.ro',
    url='https://github.com/alexei/python-addresslib',
    download_url='https://github.com/alexei/python-addresslib/archive/1.0.2.tar.gz',  # noqa
    keywords=['email address parser'],
)
