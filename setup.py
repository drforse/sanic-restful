#!/usr/bin/env python

import re
from os import path
from setuptools import setup, find_packages


requirements = [
    'aniso8601>=0.82',
    'sanic>=19.6',
    'six>=1.3.0',
    'pytz',
]


version_file = path.join(
    path.dirname(__file__),
    'sanic_restful_api',
    '__version__.py'
)
with open(version_file, 'r') as fp:
    m = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        fp.read(),
        re.M
    )
    version = m.groups(1)[0]


setup(
    name='sanic-restful-api',
    version=version,
    license='MIT',
    url='https://github.com/linzhiming0826/sanic-restful',
    author='Gimi Lin',
    author_email='120549827@qq.com',
    description='Simple framework for creating REST APIs',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite='nose.collector',
    install_requires=requirements
)
