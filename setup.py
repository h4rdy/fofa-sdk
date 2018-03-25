# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2018/3/25
# @Author  : h4rdy <with.h4rdy@gmail.com>
# @File    : setup.py

import io
import os
from setuptools import setup

NAME = 'pyfofa'
DESCRIPTION = 'Python3 library for FOFA (https://fofa.so)'
URL = 'https://github.com/h4rdy/fofa-sdk'
EMAIL = 'with.h4rdy@gmail.com'
AUTHOR = 'H4rdy'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None
REQUIRED = [
      'requests'
]


here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    author=AUTHOR,
    author_email=EMAIL,
    packages=['pyfofa'],
    url=URL,
    license='LICENSE.txt',
    description=DESCRIPTION,
    long_description=long_description,
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON
)

