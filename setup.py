#!/usr/bin/env python

from distutils.core import setup


setup(
    name='nprimes',
    version='0.0.0',
    author='Jacob Powers',
    author_email='powersjcb@gmail.com',
    package_dir={'': 'lib'},
    scripts=['lib/primes.py'],
)