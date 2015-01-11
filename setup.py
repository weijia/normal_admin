#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import normal_admin

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = normal_admin.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='normal_admin',
    version=version,
    description="""Admin site without staff role""",
    long_description=readme + '\n\n' + history,
    author='Richard',
    author_email='richardwangwang@gmail.com',
    url='https://github.com/weijia/normal_admin',
    packages=[
        'normal_admin',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='normal_admin',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)