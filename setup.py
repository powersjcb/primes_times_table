#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nprimes',
    version='0.0.0',
    author='Jacob Powers',
    author_email='powersjcb@gmail.com',
    packages=find_packages(where='lib'),
    entry_points={
        'console_scripts': [
            'genprimes = nprimes:main'
        ],
    },
)