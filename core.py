#!/usr/bin/env python3

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

from os import getenv
from sys import argv
from tkinter import *   
from libs.keys_actions import *
from PIL import Image, ImageTk


master = Tk()
master.geometry("700x700")
master.title("LuxarG")
master.minsize(height=500, width=500)
master.config(bg='black')

try:
    img = ImageTk.PhotoImage(Image.open('%s/.luxarg/icon/luxarg.png' % getenv('HOME')))
    master.iconphoto(False, img)

except:
   pass

show_status = Label() 
show_status['text']='__STOP_MODE__\nINSERT MODE : <F1> , SAVE MODE : <F2>'
show_status['bg']='black'
show_status['fg']='white'
show_status['font']=('', 13)

show_status.pack(fill='x')

# adding scrollbar
scrollbar = Scrollbar(master)

# packing scrollbar
scrollbar.pack(side=RIGHT, fill='y')

text_field = Text(master, yscrollcommand=scrollbar.set)
text_field.pack(expand=True, fill=BOTH)
text_field.focus()



text_field.bind('<F1>', lambda e :  insert_mode(master, text_field, show_status, '__INSERT_MODE__'))
text_field.bind('<Escape>', lambda e :  stop_mode(master, text_field, show_status, '__STOP_MODE__'))
text_field.bind('<F2>', lambda e :  save_mode(master, text_field, show_status, '__SAVE_MODE__'))
text_field.bind('<F3>', lambda e: open_mode(master, text_field, show_status, '__OPEN_MODE__'))

try:
    try:
        text_field.configure(stat='normal')
        fin = open(argv[1], 'r')
        text_field.delete('1.0', 'end')
        text_field.insert('1.0', fin.read())
        show_status['text']='__OPEN_MODE__\nINSERT MODE : <F1> , SAVE MODE : <F2>'
        text_field.configure(state='disabled')

        fin.close()

    except OSError as error:
        from libs.read_write import message
        message('', str(error)[10:])
except:
    pass

# DISABLE text box 
text_field.configure(state='disabled')

text_field.config(bg='black', fg='white', 
                padx=15, pady=0, 
                relief=SUNKEN, 
                insertbackground='yellow', insertborderwidth=1,
                font=('', 20)
                )


# text_field
# configuring the scrollbar
scrollbar.config(bg='gray', command=text_field.yview)


master.mainloop()
