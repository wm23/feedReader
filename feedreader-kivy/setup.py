from distutils.core import setup


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
    name='feedreader-kivy',
    version='0.0.1',
    packages=['feedreader'],
    install_requires = [
      'feedreader-base', 
      'cython', 
      'pygame',
      'kivy'
    ],
    dependency_links=[
        "hg+http://bitbucket.org/pygame/pygame#egg=pygame",
        'file:../feedreader-base#egg=feedreader-base'
    ],
    url='',
    license='',
    author='Wojciech Miga',
    author_email='wojciech.miga@gmail.com',
    description='',
    package_dir = {'feedreader.ui': 'src/feedreader/ui/', 'feedreader': 'src/feedreader'},
    tests_require=['pytest'],
    cmdclass={'test': PyTest}

)
