from os import system
from tkinter import *
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
    save_mode_window.title('Please enter your PATH : ')
    save_mode_window.resizable(False, False)
    save_mode_window.geometry('400x40')
    
    # show stop mode status
    show_status['text'] = '%s\nSAVE path example : /tmp/file_name.txt' % status
    
    # for store all the save_path variable
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
