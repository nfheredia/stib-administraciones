#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import stib-administraciones
version = stib-administraciones.__version__

setup(
    name='stib-administraciones',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'stib-administraciones',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['stib-administraciones/manage.py'],
)
