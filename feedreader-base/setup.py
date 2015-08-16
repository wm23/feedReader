from distutils.core import setup

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

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
    name='feedreader-base',
    version='0.0.1',
    packages=['feedreader', 'feedreader.lib'],
    url='',
    license='',
    author='Wojciech Miga',
    author_email='wojciech.miga@gmail.com',
    description='',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    package_dir = {'feedreader.lib': 'src/feedreader/lib/', 'feedreader': 'src/feedreader'},
)
