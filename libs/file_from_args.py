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

def open_mode_by_arg(text_field, show_status, io_mode, path_arg):
    '''$ luxarg file_path/filename.txt'''
    text_field.configure(stat='normal')

    # open file with read mode
    fin = open(path_arg, io_mode)

    #insert from file
    text_field.delete('1.0', 'end')
    text_field.insert('1.0', fin.read())

    #change status
    show_status['text']='__OPEN_MODE__\nHELP MODE : <F4>'
    text_field.configure(state='disabled')

    # close the file
    fin.close()
