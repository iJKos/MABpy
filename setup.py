# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'MABpy',
    packages = ['MABpy'], # this must be the same as the name above

    version = '0.1-alpha',
    description = 'The multi-armed bandit problem models library and various strategies analysis.',
    long_description=long_description,

    url = 'https://github.com/iJKos/MABpy', # use the URL to the github repo

    author = 'iJKos',
    author_email = 'JK.Ermakov@gmail.com',

    license='MIT',

    download_url = 'https://github.com/iJKos/MABpy/releases/tag/v0.1-alpha',
    keywords = ['MultiArmedBandits', 'ReinforsmentLearning'], # arbitrary keywords
    classifiers = [
      'Development Status :: 3 - Alpha',

      # Pick your license as you wish (should match "license" above)
      'License :: OSI Approved :: MIT License',

      # Specify the Python versions you support here. In particular, ensure
      # that you indicate whether you support Python 2, Python 3 or both.
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
    ],

    install_requires=['numpy'],
)
