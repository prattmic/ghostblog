#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ghostblog',
      version='0.1.0',
      description='Python Ghost API wrapper',
      author='Michael Pratt',
      author_email='michael@pratt.im',
      url='https://github.com/prattmic/ghostblog',
      packages=['ghostblog'],
      install_requires=['oauthlib', 'requests_oauthlib'],
      license='MIT',
)
