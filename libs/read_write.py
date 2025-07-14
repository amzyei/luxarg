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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from os import path
from . import keys_actions


def message(path_msg, text_msg):
    dialog = None
    if text_msg == 'saved !':
        dialog = Gtk.MessageDialog(
            None,
            0,
            Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK,
            text_msg
        )
        dialog.format_secondary_text(f"{path_msg}  {text_msg}")
    else:
        dialog = Gtk.MessageDialog(
            None,
            0,
            Gtk.MessageType.ERROR,
            Gtk.ButtonsType.OK,
            text_msg
        )
        dialog.format_secondary_text(f"{path_msg}  {text_msg}")

    dialog.run()
    dialog.destroy()


def writer(path_and_filename, text, widget_destroy):
    
    # path_and_filename equal to EMPTY 
    if path_and_filename == '':
        path_and_filename = 'Field is empty !\nPlease HIT <F2> and enter your file name again ...'
        message(path_and_filename, '')

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file 
        message(path_and_filename, ': Is directory')   
    
    else:
        
        try:
            with open(path_and_filename, 'w') as fin:
                fin.write(text)
            message(path_and_filename, 'saved !')
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
    

    return widget_destroy.destroy()



# read a file 
def reader(path_and_filename, text_field, widget_destroy=None):

    # clear the buffer before open file 
    buffer = text_field.get_buffer()
    buffer.set_text("")

    # path_and_filename equal to EMPTY 
    if path_and_filename == '':
        path_and_filename = 'Field is empty !\nPlease HIT <F2> and enter your path and file name again ...'
        message(path_and_filename, '')
        

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file 
        message(path_and_filename, ': Is directory (Directory is not readable)')   
        

    # if a file 
    else:
        try:
            with open(path_and_filename, 'r') as fin:
                readed = fin.read()
        except OSError as error:
            message('', str(error)[10:])
            readed = ""
        
    try:    
        buffer.set_text(str(readed))
    except:
        pass
        
    return widget_destroy.destroy()

