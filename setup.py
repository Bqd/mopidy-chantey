from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='Mopidy-Chantey',
    version=get_version('mopidy_chantey/__init__.py'),
    url='https://github.com/Bqd/mopidy-chantey',
    license='Apache License, Version 2.0',
    author='bastien lemeunier',
    author_email='bastien.lemeunier@gmail.com',
    description='collaborative radio',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'chantey = mopidy_chantey:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
