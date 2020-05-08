# -*- coding: utf-8 -*-
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rqt_virtual_joy'],
    scripts=['scripts/rqt_virtual_joy'],
    package_dir={'': 'src'},
)

setup(**d)git reset --hard HEAD^