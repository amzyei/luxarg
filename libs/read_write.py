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

from tkinter import messagebox
from os import chdir, path, read, register_at_fork, stat, system
from . import keys_actions


def message(path_msg, text_msg):


    if text_msg == 'saved !':
        msg = messagebox.showinfo('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))
    
    else:
        msg = messagebox.showerror('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))


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
            fin = open(path_and_filename, 'w')
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except:
            message(path_and_filename, 'not saved ! %s' % 
            OSError('Invalid path input!\nExample :\n/tmp/file_name.txt'))

    return widget_destroy.destroy()


# render the TRUE path file 
def file_status(path_and_filename):
    
    # check file 
    if path.isfile(path_and_filename):
        return path_and_filename
    else:
        return  ''

# read a file 
def reader(path_and_filename, file_status, text_field, widget_destroy):

    # delete all the buffer and after open file 
    text_field.delete('1.0', 'end')
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

            fin = open(path_and_filename, 'r')
            readed =  fin.read()
            fin.close()
        
        except:
            message(path_and_filename, '%s' % 
            OSError('Invalid path input!\nExample :\n/tmp/file_name.txt'))
            
    try:    
        text_field.insert('1.0', str(readed))
        text_field.configure(state='disabled')
        
    
    except:
        text_field.configure(state='disabled')
        
    return widget_destroy.destroy()

