#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import stib_administraciones
version = stib_administraciones.__version__

setup(
    name='stib_administraciones',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'stib_administraciones',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['stib_administraciones/manage.py'],
)
