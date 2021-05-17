#!/usr/bin/python3 

''' 

Short description of this Python module.
Longer description of this module.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

'''

import urwid
from os import system, getenv

def quit(key):
    if key in 'q':
        raise urwid.ExitMainLoop()

# if system('cp -rf . ~/.luxarg ; sudo ln -s %s/.luxarg/core.py /usr/bin/luxarg' % getenv('HOME')) == 0:
if (system('cp -rf . ~/.luxarg')) == 0:
    txt = urwid.Text(u'Luxarg INSTALLED successfuly !\nfor quit : \'q\'', align='left')
    fill = urwid.Filler(txt, 'middle')
    loop = urwid.MainLoop(fill, unhandled_input=quit)
    loop.run()
    
else:
    print('broken !')

