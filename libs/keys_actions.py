from tkinter import *

def insert_mode(master, text_field, show_status, status ):
    
    show_status['text'] = status

    return text_field.configure(state='normal'), show_status