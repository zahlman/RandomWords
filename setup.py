# -*- coding: utf-8 -*-

import sys

from setuptools import setup
try:
    from setuptools.command.test import test as TestCommand
except ImportError:
    # setuptools.command.test has been removed.
    # Since we can't define `PyTest`, there are no `cmdclass`es to use.
    CMDCLASS = {}
else:
    class PyTest(TestCommand):
        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = ['--strict-markers', '--verbose', '--tb=long']
            self.test_suite = True

        def run_tests(self):
            import pytest
            errcode = pytest.main(self.test_args)
            sys.exit(errcode)
    # Use `PyTest` as a `cmdclass`.
    CMDCLASS = {'test': PyTest}


setup(
    tests_require=['pytest'],
    cmdclass=CMDCLASS,
    test_suite='random_words.test.test_random_words',
    extras_require={ 'testing': ['pytest'] },
)
