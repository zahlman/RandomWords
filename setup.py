# -*- coding: utf-8 -*-

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='RandomWords',
    version='0.1.10',
    author='Tomek Święcicki',
    author_email='tomislater@gmail.com',
    packages=['random_words'],
    url='https://github.com/tomislater/RandomWords',
    license='LICENSE.txt',
    description='A useful module for a random text, e-mails and lorem ipsum.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
    ],
    include_package_data=True,
    install_requires=['ujson'],
    tests_require=['pytest', 'pytest-cov'],
    cmdclass={'test': PyTest},
    test_suite='random_words.test.test_random_words',
    extras_require={
        'testing': ['pytest', 'pytest-cov'],
    },
)
