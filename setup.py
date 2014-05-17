# -*- coding:utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

install_requires=[
    'setuptools',
    'pyramid', 
    'korpokkur'
    ]

setup(name='korpokkur.sandbox',
      version='0.0.0',
      description='individual scaffold set',
      long_description='individual scaffold set',
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        ],
      keywords='scaffold',
      author="",
      author_email="",
      url="",
      namespace_packages=["korpokkur"],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = install_requires,
      entry_points = """      [korpokkur.scaffold]
      pyramid = korpokkur.pyramid:Package
      """
      )
