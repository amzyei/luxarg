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

from os import read, stat, system
from tkinter import *  
from tkinter.messagebox import showerror
from . import read_write

# insert mode 
def insert_mode(master, text_field, show_status, status ):
    # show insert mode status
    show_status['text'] = '%s\nSTOP MODE : <ESC> , SAVE MODE : <F2>' % status
    
    #return all 
    return text_field.configure(state='normal'), show_status


# stop mode 
def stop_mode(master, text_field, show_status, status ):
    
    # show stop mode status

    show_status['text'] = '%s\nSAVE MODE : <F2> , INSERT MODE : <F1>' % status


    # return all 
    return text_field.configure(state='disabled'), show_status


# stop mode 
def save_mode(master, text_field, show_status, status ):
    
    # save mode box for user input 
    save_mode_window = Toplevel(master)
    save_mode_window.title('Please enter your PATH and FILE NAME (SAVE):')
    save_mode_window.resizable(False, False)
    save_mode_window.geometry('400x25')
    
    # show stop mode status
    show_status['text'] = '%s\nSAVE path example : /tmp/file_name.txt' % status
    
    # for storing all the save_path variable value
    save_path = Entry(save_mode_window, font=('', 13))
    save_path.config(bg='black', fg='white')
    save_path.focus()
    save_path.pack(fill=BOTH)

    # save file with ENTER
    save_path.bind('<Return>', lambda e : 
        read_write.writer(save_path.get().strip(),
        text_field.get('1.0', 'end').strip(),
        save_mode_window)
    )

    # return all 
    return text_field.configure(state='disabled'), show_status


def open_mode(master, text_field, show_status, status):


    open_file_window = Toplevel(master)
    open_file_window.title('Please enter your PATH and FILE NAME (OPEN):')
    open_file_window.resizable(False, False)
    open_file_window.geometry('400x25')
    
    # for storing all the file_path variable value
    file_path = Entry(open_file_window, font=('', 13))
    file_path.config(bg='black', fg='white')
    file_path.pack(fill=BOTH)
    file_path.focus()
    
    # open file with ENTER
    file_status = ''
    file_path.bind('<Return>', 
        lambda e : read_write.reader(file_path.get().strip(), file_status, text_field, open_file_window)
    )
    
    # show open mode status
    show_status['text'] = '%s\nSAVE MODE : <F2> , INSERT MODE : <F1>' % status

    # return all
    return show_status, text_field.configure(state='normal')

# def font_up(text_field, font_size):
    
#     font_size = font_size

#     return text_field.config(font=('', font_size + 1))

