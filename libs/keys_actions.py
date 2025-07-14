import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from . import read_write

# insert mode 
def insert_mode(master, text_field, show_status, status ):
    # show insert mode status
    show_status.set_text('%s\nSTOP MODE : <ESC> , SAVE MODE : <F2>' % status)
    
    #return all 
    text_field.set_editable(True)
    return text_field, show_status


# stop mode 
def stop_mode(master, text_field, show_status, status ):
    
    # show stop mode status

    show_status.set_text('%s\nSAVE MODE : <F2> , INSERT MODE : <F1>' % status)


    # return all 
    text_field.set_editable(False)
    return text_field, show_status


# stop mode 
def save_mode(master, text_field, show_status, status ):
    
    # save mode box for user input 
    save_mode_window = Gtk.Window(title='PATH and FILE NAME (SAVE):')
    save_mode_window.set_resizable(False)
    save_mode_window.set_default_size(500, 25)
    
    # show stop mode status
    show_status.set_text('%s\nSAVE path example : /tmp/file_name.txt' % status)
    
    # for storing all the save_path variable value
    save_path = Gtk.Entry()
    save_path.set_property("primary-icon-name", "document-save")
    save_path.set_hexpand(True)
    save_path.set_margin_top(2)
    save_path.set_margin_bottom(2)
    save_path.set_margin_start(2)
    save_path.set_margin_end(2)
    save_path.grab_focus()
    
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    box.pack_start(save_path, True, True, 0)
    save_mode_window.add(box)
    save_mode_window.show_all()

    # save file with ENTER
    def on_save_path_activate(entry):
        read_write.writer(entry.get_text().strip(),
        text_field.get_buffer().get_text(text_field.get_buffer().get_start_iter(), text_field.get_buffer().get_end_iter(), True).strip(),
        save_mode_window)
    save_path.connect("activate", on_save_path_activate)

    # return all 
    text_field.set_editable(False)
    return text_field, show_status


def open_mode(master, text_field, show_status, status):


    open_file_window = Gtk.Window(title=' PATH and FILE NAME (OPEN):')
    open_file_window.set_resizable(False)
    open_file_window.set_default_size(450, 25)
    
    # for storing all the file_path variable value
    file_path = Gtk.Entry()
    file_path.set_property("primary-icon-name", "document-open")
    file_path.set_hexpand(True)
    file_path.set_margin_top(2)
    file_path.set_margin_bottom(2)
    file_path.set_margin_start(2)
    file_path.set_margin_end(2)
    file_path.grab_focus()
    
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    box.pack_start(file_path, True, True, 0)
    open_file_window.add(box)
    open_file_window.show_all()

    # open file with ENTER
    def on_file_path_activate(entry):
        read_write.reader(entry.get_text().strip(),  text_field, open_file_window)
    file_path.connect("activate", on_file_path_activate)
    
    # show open mode status
    show_status.set_text('%s\nSAVE MODE : <F2> , INSERT MODE : <F1>' % status)

    # return all
    text_field.set_editable(True)
    return show_status, text_field
