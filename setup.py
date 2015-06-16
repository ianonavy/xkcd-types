#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='xkcd_types',
      version='0.1',
      description='Implementation of https://xkcd.com/1537/',
      author='Ian Naval',
      author_email='ianonavy@gmail.com',
      url='https://github.com/ianonavy/xkcd-types',
      install_requires=['antlr4-python3-runtime'],
      scripts=['scripts/xkcdtypes'],
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]))
