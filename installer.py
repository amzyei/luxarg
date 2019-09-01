#!/usr/bin/python3 
from os import system, getenv

if system('cp -rf . ~/.luxarg ; sudo ln -s %s/.luxarg/core.py /usr/bin/luxarg' % getenv('HOME')) == 0:
    print('LUXARG installed')
else:
    print('broken !')

