#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name             = 'hoge',
    version          = '0.0.1',
    description      = 'hoge description',
    license          = 'MIT',
    author           = 'mihyaeru21',
    author_email     = 'mihyaeru21@gmail.com',
    url              = 'https://github.com/mihyaeru21/python_hoge_command',
    keywords         = 'hoge command python',
    packages         = ['hoge'],
    entry_points     = {'console_scripts': ['hoge = hoge:main']},
    install_requires = [],
)

