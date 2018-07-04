from distutils.core import setup

setup(
    name='blinky',
    version='0.1',
    author='Jonas Große Sundrup',
    author_email='cherti@letopolis.de',
    packages=['blinky'],
    scripts=['scripts/blinky'],
    url='https://github.com/cherti/blinky',
    license='GPLv3',
    description='AUR-helper with minimal hassle',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown"
)