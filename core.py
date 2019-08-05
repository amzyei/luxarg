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

from tkinter import *
from libs.keys_actions import *
master = Tk()
master.geometry("700x700")
master.title("LuxarG")
master.minsize(height=500, width=500)
master.config(bg='black')


# show_status = LabelFrame(master, bg='black', foreground='white', 
# text='Please HIT <F1> for "INSERT MODE"', 
# font=('', 13)).pack(fill=X)

show_status = Label() 
show_status['text']='Please HIT <F1> for INSERT MODE'

show_status.pack(fill='x')

# adding scrollbar
scrollbar = Scrollbar(master)

# packing scrollbar
scrollbar.pack(side=RIGHT, fill='y')

text_field = Text(master, yscrollcommand=scrollbar.set)
text_field.pack(expand=True, fill=BOTH)
text_field.focus()

# DISABLED text box 
text_field.configure(state='disabled')

text_field.bind('<F1>', lambda e :  insert_mode(master, text_field, show_status, '__INSERT_MODE__'))
text_field.bind('<Escape>', lambda e :  stop_mode(master, text_field, show_status, '__STOP_MODE__'))


text_field.config(bg='black', fg='lightgray', 
                padx=15, pady=0, 
                relief=SUNKEN, font=('', 20), 
                insertbackground='yellow', insertborderwidth=1,
                
                )


# text_field
# configuring the scrollbar
scrollbar.config(bg='gray', command=text_field.yview)


master.mainloop()
