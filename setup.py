#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fdbutils.
# https://github.com/cdecu/fdb-utils

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 1992-2016, Carlos de Cumont <carlos@decumont.be>

from setuptools import setup, find_packages
import fdbutils

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='fdbutils',
    version=fdbutils.__version__,
    description='Firebird Metadata,Doc,Generator,...  Utils',
    long_description=open('README.md').read(),
    keywords='Firebird Metadata FDB',
    author='Carlos de Cumont',
    author_email='carlos@decumont.be',
    url='https://github.com/cdecu/fdbutils',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    package_dir={'fdbutils': 'fdbutils'},
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
        'fdb>=1.5.1'
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'fdbutils = fdbutils.console:generate',
        ],
    },
)
