#!/usr/bin/env python3


from tkinter import messagebox
from os import path
from os import  getcwd


def message(path_msg, text_msg):
    ''' status message from IO UNIT '''
    if text_msg == 'saved !':
        messagebox.showinfo('%s'%text_msg,
        message='%s  %s' %(path_msg, text_msg))

    else:
        messagebox.showerror('%s'%text_msg,
        message='%s  %s' %(path_msg, text_msg))


####################################################
# IO
####################################################
def io_luxarg(path_and_filename, text, io_mode, text_field):
    ''' Input and Output UNIT '''

    # if ~/<*>.<txt/py/c/cpp/...>
    if path_and_filename[:2]=='~/':

        path_and_filename = path_and_filename.replace('~/', '%s/' %
        str(path.expanduser('~').strip()))

    elif path_and_filename[0] not in ['/', '.', '~']:
        path_and_filename = '%s/%s'%(getcwd(), path_and_filename)   
        path_and_filename = path_and_filename.strip()

    # path_and_filename equal to EMPTY
    if path_and_filename == '':
        path_and_filename = 'Field is empty ...!'

        message(path_and_filename, '')
    elif path_and_filename == '~':
        message(path_and_filename, ': Is directory (Directory is not readable)')

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file
        message(path_and_filename, ': Is directory (Directory is not readable)')
    


    elif io_mode == 'r':
        # delete all the buffer and after open file
        text_field.delete('1.0', 'end')



        try:
            with open(path_and_filename, io_mode) as fin:
                readed =  fin.read()
                text_field.insert('1.0', str(readed))
                text_field.configure(state='disabled')

        except UnicodeDecodeError as unicode:
            message(path_and_filename, str(unicode))

        except FileNotFoundError as error:
            message('', str(error)[10:])

        except OSError as error:
            message('', str(error)[10:])


        text_field.configure(state='disabled')

    # relational path for home
    elif io_mode=='w':
        path_and_filename = path_and_filename.replace('~/','%s/'%
        str(path.expanduser('~'))).strip()

        try:
            fin = open(path_and_filename, io_mode)
            fin.write(text)
            message(path_and_filename, 'saved !')
            fin.close()

        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
        

    return text_field.focus()
