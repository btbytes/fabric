#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

from fabric.version import get_version


readme = open('README').read()

long_description = """
To find out what's new in this version of Fabric, please see `the changelog
<http://docs.fabfile.org/changes/%s.html>`_.

----

%s

----

For more information, please see the Fabric website or execute ``fab --help``.
""" % (get_version('short'), readme)

# PyCrypto>2.0 + Python 2.5 + pip == bad times.
# We can't easily detect pip usage at this point, but we can at least limit our
# "downgrade" of the PyCrypto requirement to 2.5-only.
PYCRYPTO = "<2.1" if (sys.version_info[:2] == (2, 5)) else ">=1.9"

setup(
    name='Fabric',
    version=get_version('short'),
    description='Fabric is a simple, Pythonic tool for remote execution and deployment.',
    long_description=long_description,
    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',
    url='http://fabfile.org',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose', 'fudge'],
    install_requires=['pycrypto %s' % PYCRYPTO, 'paramiko >=1.7.6'],
    entry_points={
        'console_scripts': [
            'fab = fabric.main:main',
        ]
    },
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Clustering',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
    ],
)
