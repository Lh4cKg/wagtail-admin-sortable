#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from wagtail_adminsortable import __version__


def read(filename):
    with open(filename, encoding='utf-8') as fd:
        return fd.read()


setup(
    name='wagtail_adminsortable',
    version=__version__,
    author='Lasha Gogua',
    author_email='gogualasha@gmail.com',
    description='Generic drag-and-drop sorting for the List Views in the Wagtail Admin interface.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Lh4cKg/wagtail-admin-sortable',
    license='MIT',
    keywords=['django', 'wagtail'],
    platforms=['OS Independent'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Framework :: Wagtail',
    ],
    install_requires=[
        "wagtail>=6",
        "wagtail-modeladmin",
    ],
    packages=find_packages(exclude=['example', 'docs']),
    include_package_data=True,
    zip_safe=False,
)
