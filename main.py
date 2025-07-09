#!/usr/bin/env python3

'''
AMZY-0 (M.Amin Azimi .K)
Copyright (C) 2019-2021 luxarg AMZY-0 (M.Amin Azimi .K) and contributors

Luxarg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Luxarg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
This file is part of Luxarg.
Luxarg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Luxarg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License

'''
from os import path, getenv
from sys import argv, exit
from tkinter import BOTH, RIGHT, SUNKEN, Tk, Text, Scrollbar,Label, Entry
from libs.keys_actions import *
from PIL import Image, ImageTk
from libs.read_write import message
from libs.file_from_args import open_mode_by_arg
from libs.counter import linenum

help_contents = '''

INSERT MODE : <F1>
SAVE   MODE : <F2>
OPEN   MODE : <F3>
HELP   MODE : <F4>
DELETE ALL  : <Ctrl + 0>
SELECT ALL  : <Ctrl + />
CORSUR RIGHT: <Ctrl + f> move the cursor forward one space.
CORSUR LEFT : <Ctrl + b> move the cursor backward one space.
Copy        : <Ctrl + c>
Paste       : <Ctrl + v>
Cut         : <Ctrl + w>
UNDO        : <Ctrl + z>
REDO        : <Ctrl + Shift + z>
HELP   CLI  : luxarg <-h/--help>
ZOOM IN     : <Ctrl + equal(=)>
ZOOM OUT    : <Ctrl + minus(-)>

'''




master = Tk()
master.geometry("700x700")
master.title("LuxarG")
master.minsize(height=500, width=500)
master.config(bg='black')

show_status = Label()
show_status['text']='__STOP_MODE__\nHELP MODE : <F4>'
show_status['bg']='black'
show_status['fg']='white'
show_status['font']=('', 13)

#for line status
showline_stat = Label()
showline_stat['bg']='black'
showline_stat['fg']='white'
showline_stat['font']  = ('', 12)
showline_stat.pack(fill='y')

show_status.pack(fill='x')


# for storing all the file_path variable value
# global file_path
file_path = Entry(master, font=('', 13))

# "file_path" configure :
file_path.configure(bg='black',
    fg='white',
    insertbackground='yellow',
)

file_path.insert(0, 'file path example : /tmp/tmp')
file_path.pack(fill=BOTH)

# adding scrollbar
scrollbar = Scrollbar(master)

# packing scrollbar
scrollbar.pack(side=RIGHT, fill='y')

# definition a text_field
text_field = Text(master, yscrollcommand=scrollbar.set, undo=True)
text_field.pack(expand=True, fill=BOTH)
text_field.focus()


if argv[0] and len(argv) ==1:
    pass
elif argv[1] == '-h' or argv[1]=='--help':
    print(help_contents)

    master.forget(master)
    exit()

try:
    try:
        # try to set logo
        img = ImageTk.PhotoImage(Image.open('%s/.luxarg/icon/luxarg.png'%getenv('HOME')))
        master.iconphoto(False, img)

    except:
        # local loading (LOGO)
        img = ImageTk.PhotoImage(Image.open('./icon/luxarg.png'))
        master.iconphoto(False, img)

except:
    pass

# set font size to 20
font_size = 20

def font_resizer(component, minesOrPlus):
    '''font resizer'''
    global font_size


    if minesOrPlus == '+' and font_size <= 100:
        component['font'] = ('', font_size + 1)
        font_size += 1
    elif minesOrPlus == '-' and font_size >= 10 :
        component['font'] = ('', font_size - 1)
        font_size -= 1

        return component['font']



#####################################################
#                                                   #
#                  key binding                      #
#                                                   #
#####################################################



# INSERT MODE (binding F1)
text_field.bind('<F1>', lambda e :  insert_mode(
    text_field,
    show_status,
    '__INSERT_MODE__'
    )
)
# STOP MODE (binding ESC)
text_field.bind('<Escape>', lambda e :  stop_mode(
    text_field,
    show_status,
    '__STOP_MODE__'
    )
)

# SAVE MODE (binding F2)
text_field.bind('<F2>', lambda e :  save_mode(
    text_field,
    show_status,
    '__SAVE_MODE__',
    file_path
    )
)

# OPEN MODE (binding F3)
text_field.bind('<F3>', lambda e: open_mode(
    text_field,
    show_status,
    '__OPEN_MODE__',
    file_path
    )
)

# HELP MODE (binding F4)
text_field.bind('<F4>', lambda e: help_mode(
    master,
    show_status,
    '__HELP_MODE__',
    help_contents
    )
)

# UNDO
text_field.bind('<Control-Z>', lambda e : text_field.edit_undo)

# REDO
text_field.bind('<Control-Shift-Z>', lambda e : text_field.edit_redo)

# zoom control by CTRL + Mouse scroll
# text_field.bind('<Control-Button-4>', lambda e : font_resizer(text_field, '+'))
# text_field.bind('<Control-Button-5>', lambda e : font_resizer(text_field, '-'))
text_field.bind('<Control-equal>', lambda e : font_resizer(text_field, '+'))
text_field.bind('<Control-minus>', lambda e : font_resizer(text_field, '-'))

# delete all with CTRL + 0
text_field.bind('<Control-0>', lambda e :text_field.delete('1.0', 'end'))


# key binding for calc lines
text_field.bind('<BackSpace>', lambda e: linenum(text_field, showline_stat))
text_field.bind('<Return>', lambda e : linenum(text_field, showline_stat))
text_field.bind('<KP_Enter>', lambda e : text_field.insert('end', '\n'),
linenum(text_field, showline_stat))
text_field.bind('<KeyRelease>', lambda e: linenum(text_field, showline_stat))



try:
    # try open file from the arg1 (like this : $ luxarg /tmp/tmp)
    try:
        open_mode_by_arg(text_field, show_status, 'r', argv[1])
        file_path.delete(0, 'end')
        file_path.insert(0, str(path.expanduser(argv[1])))
        linenum(text_field, showline_stat)
    # if pass is not true
    except OSError as error:
        message('', str(error)[10:])
        text_field.focus()
except:
    pass

# DISABLE text box
text_field.configure(state='disabled')

# tab setting

# text field configuration

text_field.config(bg='black', fg='white',
                relief=SUNKEN,
                spacing1=10,
                insertbackground='yellow',
                insertborderwidth=1,
                padx=20,
                pady=4,
                font=('', font_size),
                )


# configuring the scrollbar
scrollbar.config(bg='black', command=text_field.yview)

master.mainloop()
