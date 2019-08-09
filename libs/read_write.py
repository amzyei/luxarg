from tkinter import messagebox
from os import chdir, path, system

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
    
    elif path.isabs(path_and_filename):
        
        message(path_and_filename, ': Invalid path input!\nExample :\n/tmp/file_name.txt')   
        
    
    else:
        system(' touch %s' % path_and_filename) 
        fin = open(path_and_filename, 'w')
        
        try:
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except:
            message(path_and_filename, 'not saved !')

    widget_destroy.destroy()
