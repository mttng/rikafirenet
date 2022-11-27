#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding="utf-8") as history_file:
    history = history_file.read()

requirements = ['Click>=7.0']

test_requirements = [ ]

setup(
    author="Mathieu Tanguy",
    author_email='mathieu@tanguym.eu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python package that dialogs with Rika pellet stove (under dev)",
    entry_points={
        'console_scripts': [
            'rikafirenet=rikafirenet.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='rikafirenet',
    name='rikafirenet',
    packages=find_packages(include=['rikafirenet', 'rikafirenet.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mttng/rikafirenet',
    version='0.0.4',
    zip_safe=False,
)
