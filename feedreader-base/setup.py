from distutils.core import setup

setup(
    name='feedreader-base',
    version='0.0.1',
    packages=['feedreader', 'feedreader.lib'],
    url='',
    license='',
    author='Wojciech Miga',
    author_email='wojciech.miga@gmail.com',
    description='',
    package_dir = {'feedreader.lib': 'src/feedreader/lib/', 'feedreader': 'src/feedreader'},
)
