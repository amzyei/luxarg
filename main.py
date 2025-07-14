#!/usr/bin/env python3

'''
Refactored main.py to use Gtk (python3) in procedural style without OOP.
Modernized UI with integrated mode display using emojis.
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
from sys import argv
from os import getenv
from libs.keys_actions import insert_mode, stop_mode, save_mode, open_mode
from libs.read_write import message

def main():
    # Create main window
    master = Gtk.Window(title="LuxarG")
    master.set_default_size(700, 700)
    master.set_size_request(500, 500)
    master.set_resizable(True)

    # Set window icon
    try:
        # Try to load icon from /opt/luxarg/icon/luxarg.png
        master.set_icon_from_file('/opt/luxarg/icon/luxarg.png')
    except Exception:
        pass

    # Create vertical box container
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    master.add(vbox)

    # Create toolbar box
    toolbar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    toolbar.set_margin_top(5)
    toolbar.set_margin_bottom(5)
    toolbar.set_margin_start(5)
    toolbar.set_margin_end(5)
    vbox.pack_start(toolbar, False, False, 0)

    # Mode label with emoji
    show_status = Gtk.Label(label="⏹️ STOP MODE | 📝 INSERT MODE: F1 | 💾 SAVE MODE: F2 | 📂 OPEN MODE: F3")
    show_status.set_justify(Gtk.Justification.LEFT)
    show_status.set_name("status_label")
    toolbar.pack_start(show_status, True, True, 0)

    # Create scrolled window
    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    vbox.pack_start(scrolled_window, True, True, 0)

    # Create text view
    text_field = Gtk.TextView()
    text_field.set_wrap_mode(Gtk.WrapMode.WORD)
    text_field.set_editable(False)
    text_field.set_cursor_visible(True)
    text_field.set_left_margin(15)
    text_field.set_right_margin(15)
    import gi.repository.Pango as Pango
    text_field.modify_font(Pango.font_description_from_string("Monospace 20"))
    scrolled_window.add(text_field)

    # Get text buffer
    buffer = text_field.get_buffer()

    # Key press event handler
    def on_key_press(widget, event):
        keyval = event.keyval
        state = event.state
        # Map keys to functions
        # F1
        if keyval == Gdk.KEY_F1:
            insert_mode(master, text_field, show_status, '__INSERT_MODE__')
            show_status.set_text("📝 INSERT MODE | ⏹️ STOP MODE: ESC | 💾 SAVE MODE: F2 | 📂 OPEN MODE: F3")
            return True
        # Escape
        elif keyval == Gdk.KEY_Escape:
            stop_mode(master, text_field, show_status, '__STOP_MODE__')
            show_status.set_text("⏹️ STOP MODE | 📝 INSERT MODE: F1 | 💾 SAVE MODE: F2 | 📂 OPEN MODE: F3")
            return True
        # F2
        elif keyval == Gdk.KEY_F2:
            save_mode(master, text_field, show_status, '__SAVE_MODE__')
            show_status.set_text("💾 SAVE MODE | 📝 INSERT MODE: F1 | ⏹️ STOP MODE: ESC | 📂 OPEN MODE: F3")
            return True
        # F3
        elif keyval == Gdk.KEY_F3:
            open_mode(master, text_field, show_status, '__OPEN_MODE__')
            show_status.set_text("📂 OPEN MODE | 📝 INSERT MODE: F1 | ⏹️ STOP MODE: ESC | 💾 SAVE MODE: F2")
            return True
        return False

    master.connect("key-press-event", on_key_press)

    # Load file content if provided
    if len(argv) > 1:
        try:
            with open(argv[1], 'r') as fin:
                text = fin.read()
            buffer.set_text(text)
            show_status.set_text("📂 OPEN MODE | 📝 INSERT MODE: F1 | ⏹️ STOP MODE: ESC | 💾 SAVE MODE: F2")
            text_field.set_editable(False)
        except OSError as error:
            message('', str(error)[10:])
    else:
        text_field.set_editable(False)

    # Show all widgets
    master.show_all()

    # Connect destroy signal
    master.connect("destroy", Gtk.main_quit)

    Gtk.main()

if __name__ == "__main__":
    main()
