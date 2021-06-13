
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

from os import system, getenv
system('pip install -r requirements.txt')

import urwid

# quit from installed message
def quit(key):
    if key in 'q':
        raise urwid.ExitMainLoop()

if (system('cp -rf . ~/.luxarg ; sudo ln -s %s/.luxarg/core.py /usr/bin/luxarg' % getenv('HOME'))) == 0:
    
    # install dependencies
    system('''
        sudo apt install python3-tk -y  2> /dev/null;
        sudo dnf install -y python3-tkinter -y  2> /dev/null;
        sudo pacman -S tk -y 2> /dev/null;
        sudo yum install -y tkinter  2> /dev/null;
        sudo zypper in -y python-tk 2> /dev/null;
            ''')    
    # desktop application icon for menu 
    system('sudo cp -rf ./xdg/luxarg.desktop /usr/share/applications')
    system('cp -rf ./xdg/luxarg.desktop ~/.local/share/applications')
    system("sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/")
    system("sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/")
    system("sudo cp -rf ./icon/luxarg.png /usr/share/icons/")

    # installed successfuly message
    txt = urwid.Text(u'Luxarg INSTALLED successfuly !\nfor quit : \'q\'', align='left')
    fill = urwid.Filler(txt, 'middle')
    loop = urwid.MainLoop(fill, unhandled_input=quit)
    loop.run()
    
else:
    print('status : broken !')

