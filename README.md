# luxarg :


LUXARG is a keyboard-friendly text editor.

This project started in August 2019 and was restarted in 2021.

Easy to use and user-friendly!

LUXARG supports:

- Fedora, CENTOS, and RedHat
- Debian and Ubuntu
- OpenSUSE
- Arch and Manjaro


# ICON

![ICON](icon/luxarg.png)


# Screenshot :

![screenshot](screenshot/1.png)


# KEYS : 
- INSERT MODE : <F1>
- SAVE MODE : <F2>
- OPEN MODE : <F3>


# INSTALLATION
Run the installer using the Makefile:
```
make install
```

# MAKEFILE

This project includes a `Makefile` to simplify installation and running the application.

- To install LuxarG, run:
```
make install
```
This will:
- Create the directory `/opt/luxarg/`
- Copy the project files to `/opt/luxarg/`
- Create a symlink for `main.py` as `/usr/bin/luxarg` if `main.py` exists
- Copy the desktop application icon files to the appropriate system directories

- To run the LuxarG application, use:
```
make run
```
This will execute the application by running:
```
python3 main.py
```



# Notes
This is a simple pure Python and keyboard-friendly text editor solution.
