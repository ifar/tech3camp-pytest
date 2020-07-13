#!/usr/bin/env python

from os import path
from distutils.core import setup
from setuptools import find_packages

SOURCES_ROOT = path.abspath(path.dirname(__file__))

setup(name='tech3camp-pytest',
      version='0.0.1',
      description="Pytest - Python's automated tests description",
      author='Rafal Blaczkowski',
      author_email='blaczkowski.rafal@gmail.com',
      url='https://github.com/ifar/tech3camp-pytest',
      license='GNU General Public License',
      packages=find_packages(exclude=['tests', 'tests.*']),
      install_requires=['requests'])
