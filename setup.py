import codecs
import re
from setuptools import setup
from setuptools import find_packages

version = ''
with open('pytaxa/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

with codecs.open('Changelog.rst', 'r', 'utf-8') as f:
    changes = f.read()

long_description = '\n\n' + readme + '\n\n' + changes

setup(
	name             = 'pytaxa',
	version          = version,
	description      = 'Taxonomic Classes',
	long_description = long_description,
  author           = 'Scott Chamberlain',
  author_email     = 'sckott@protonmail.com',
  url              = 'https://github.com/sckott/pytaxa',
  license          = 'MIT',
  packages         = find_packages(exclude=['test-*']),
  install_requires = ['requests>=2.19.0'],
  python_requires  = '>=3.5',
  tests_require    = ["pytest", "pytest-cov"],
  classifiers      = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
	]
)
