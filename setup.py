#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    # Name of the module
    name='py-heat-magic',

    # Details
    version='0.0.1',
    description='py-heat as IPython magic',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/csurfer/pyheatmagic',

    # Author details
    author='Vishwas B Sharma',
    author_email='sharma.vishwas88@gmail.com',

    # License
    license='MIT',
    py_modules=['heat'],
    keywords='heatmap matplotlib profiling python IPython',
    classifiers=[
        # Intended Audience.
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        # License.
        'License :: OSI Approved :: MIT License',
        # Project maturity.
        'Development Status :: 3 - Alpha',
        # Operating Systems.
        'Operating System :: POSIX',
        # Supported Languages.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # Topic tags.
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'ipython',
        'jupyter',
        'pandas',
        'sympy',
        'nose',
        'py-heat'])
