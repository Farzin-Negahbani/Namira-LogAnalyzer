import os
import sys
import platform
import shutil
from setuptools import setup
setup(
    name="loganalyzer",
    version='1.0.1',
    description='Python Script for parsing and analyzing agent2D socer simulation rcl and rcg logs',
    long_description=open("README.md").read(),
    author='Shahryar Bhm & Farzin Negahbani',
    author_email='shahryarbahmeie@gmail.com , farzin.negahbani@gmail.comh',
    url='https://github.com/Farzin-Negahbani/Namira_LogAnalyzer',
    packages=['loganalyzer', ],
    entry_points={  # Optional
        'console_scripts': [
            'loganalyzer=loganalyzer.__main__:main',
        ],
    },
)
