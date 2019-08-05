from tkinter import *

# insert mode 
def insert_mode(master, text_field, show_status, status ):
    # show insert mode status
    show_status['text'] = status
    
    #return all 
    return text_field.configure(state='normal'), show_status


# stop mode 
def stop_mode(master, text_field, show_status, status ):
    
    # show stop mode status
    show_status['text'] = status

    # return all 
    return text_field.configure(state='disabled'), show_status
