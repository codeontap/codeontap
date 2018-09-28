#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup
import re
import os
import sys


long_description = (
    "CodeOnTap is an opinionated devops framework for enterprise level CICD"
)


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """Return root package and all sub-packages."""
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(get_version("mkdocs")))
    print("  git push --tags")
    sys.exit()


setup(
    name="CodeOnTap",
    version=get_version("mkdocs"),
    url='https://www.mkdocs.org',
    license='GPL',
    description='CICD for the enterprise.',
    long_description=long_description,
    author='CodeOnTap Team',
    author_email='info@codeontap.io',  # SEE NOTE BELOW (*)
    packages=get_packages("mkdocs"),
    include_package_data=True,
    install_requires=[
        'click>=3.3',
        'Jinja2>=2.7.1',
        'livereload>=2.5.1',
        'Markdown>=2.3.1',
        'PyYAML>=3.10',
        'tornado>=5.0'
    ],
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    entry_points={
        'console_scripts': [
            'mkdocs = mkdocs.__main__:cli',
        ],
        'mkdocs.themes': [
            'readthedocs = mkdocs.themes.readthedocs',
        ],
        'mkdocs.plugins': [
            'search = mkdocs.contrib.search:SearchPlugin',
        ],
    },
    classifiers=[
    ],
    zip_safe=False,
)

# (*) Please direct queries to the discussion group:
#     https://groups.google.com/forum/#!forum/mkdocs