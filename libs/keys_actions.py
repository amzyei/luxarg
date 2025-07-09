#!/usr/bin/env python3

'''
AMZY-0 (M.Amin Azimi .K)
Copyright (C) 2019-2021 luxarg AMZY-0 (M.Amin Azimi .K) and contributors

Luxarg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Luxarg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
This file is part of Luxarg.
Luxarg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Luxarg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License'''

from tkinter import Toplevel, Label
from libs import read_write
from libs import bg_fg_color

########-#######################################################
file_mode = '\nExample : /tmp/tmp\n<ESC> for exit'

###############################################################
def insert_mode(text_field, show_status, status ):
    '''insert mode'''
    # show insert mode status
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status

    #return all
    return text_field.configure(state='normal'), show_status

###############################################################
def stop_mode(text_field, show_status, status ):
    ''' stop mode '''
    # show stop mode status

    show_status['text'] = '%s\nHELP MODE : <F4> ' % status


    # return all
    return text_field.configure(state='disabled'), show_status


###############################################################
def save_mode(text_field, show_status, status, save_path):
    ''' save mode '''
    save_path.focus()
    save_path.select_range(0, 'end')

    # save file with ENTER
    save_path.bind('<Return>', lambda e :
        read_write.io_luxarg(save_path.get().strip(),
        text_field.get('1.0', 'end').strip(),
        'w',
        text_field
        )

    )

    # go to stop mode
    show_status['text'] = '%s\nHELP MODE : <F4>%s' % (status, file_mode)

    # if the user want to leave file Entry
    save_path.bind('<Escape>', lambda e : text_field.focus())

    # return all
    return text_field.configure(state='disabled'), show_status

###############################################################
def open_mode(text_field, show_status, status, file_path):
    ''' open mode '''

    file_path.focus()
    file_path.select_range(0, 'end')

    # open file with ENTER
    file_path.bind('<Return>',
        lambda e :
        read_write.io_luxarg(
            file_path.get().strip(),
            None,
            'r',
            text_field
        )
    )

    # show open mode status
    show_status['text'] = '%s\nHELP MODE : <F4>%s' % (status, file_mode)

    file_path.bind('<Escape>', lambda e : text_field.focus())

    # return all
    return text_field.configure(state='normal'), show_status


###############################################################
def help_mode(master, show_status, status, help_contents):
    ''' help mode '''
    help_window=Toplevel(master)
    help_window.title(' LUXARG => HELP ')
    help_window.maxsize()


    help_label = Label(help_window, text=help_contents, font=('', 17))
    help_window.config(bg=bg_fg_color.bg)
    help_label.config(background=bg_fg_color.bg, foreground=bg_fg_color.fg)
    help_label.pack()
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status
    return show_status
