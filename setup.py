#!/usr/bin/python
# -*- coding: latin-1 -*-

from setuptools import setup, find_packages


setup( name='pytestpackage',
       version='1.0.0',
       author='Baroncelli Leonardo',
       author_email='leonardo.baroncelli@inaf.it',
       packages=find_packages(),
       package_dir={ 'pytestpackage': 'pytestpackage' },
       include_package_data=True
     )
