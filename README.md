# luxarg :

![issues](https://img.shields.io/github/issues/amzy-0/luxarg)

![forks](https://img.shields.io/github/forks/amzy-0/luxarg)

![stars](https://img.shields.io/github/stars/amzy-0/luxarg)

![license](https://img.shields.io/github/license/amzy-0/luxarg)


Luxarg is a keyboard-friendly text editor.

The project was started in August 2019 and restarted on June 13 at 20:14:41, 2021.

Easy to use and user-friendly!


# LUXARG support :

![](https://icons.iconarchive.com/icons/tatice/operating-systems/48/Fedora-icon.png) 
Fedora, 
![](https://icons.iconarchive.com/icons/fatcow/farm-fresh/32/centos-icon.png)
CENTOS,
![](https://icons.iconarchive.com/icons/saki/nuoveXT/48/Apps-redhat-icon.png)
RedHat,
![](https://icons.iconarchive.com/icons/tatice/operating-systems/48/Debian-icon.png)
Debian,
![](https://icons.iconarchive.com/icons/tatice/operating-systems/48/Ubuntu-icon.png)
Ubuntu, 
![](https://icons.iconarchive.com/icons/papirus-team/papirus-apps/48/distributor-logo-opensuse-icon.png)
OpenSUSE, 
![](https://icons.iconarchive.com/icons/fatcow/farm-fresh/32/arch-linux-icon.png)
Arch,
![](https://icons.iconarchive.com/icons/papirus-team/papirus-apps/48/manjaro-welcome-icon.png)
Manjaro

# ICON

![ICON](icon/luxarg.png)


# screenshot :

![screenshot](screenshot/1.png)


# Licensing

AMZY-0 (M.Amin Azimi .K) 

Copyright (C) (2019-2020-2021)  AMZY-0 (M.Amin Azimi .K) 

"Luxarg" (This program) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.



# KEYS : 

    INSERT MODE : <F1>
    SAVE   MODE : <F2>
    OPEN   MODE : <F3>
    HELP   MODE : <F4>
    DELETE ALL  : <Ctrl + 0>
    SELECT ALL  : <Ctrl + />
    CURSOR RIGHT: <Ctrl + f> move the cursor forward one space.
    CURSOR LEFT : <Ctrl + b> move the cursor backward one space.
    Copy        : <Ctrl + c>
    Paste       : <Ctrl + v>
    Cut         : <Ctrl + w>
    UNDO        : <Ctrl + z>
    REDO        : <Ctrl + Shift + z>
    HELP CLI    : luxarg <-h/--help>
    ZOOM IN     : <Ctrl + equal(=)>
    ZOOM OUT    : <Ctrl + minus(-)>

# INSTALLATION

You must install "pip" before this step ...   


    $ make 

    
# dependencies
    
    $ pip3 install -r requirements.txt

# update method
    
    $ luxarg-update (v1.0)


# Install pip
    pip.txt


# local build and execute



### INSTALL PIP BEFORE THIS OPERATIONS
****


### Step (1)
#### Ubuntu & Debian
        $ sudo apt install python3-tk -y  



#### Fedora
	    $ sudo dnf install -y python3-tkinter 



#### Arch
	    $ sudo pacman -S tk 



#### CentOS
	    $ sudo yum install -y python3-tkinter 



#### OpenSUSE
	    $ sudo zypper in -y python-tk 
    

### Step (2)
#### Install dependancies (BY PIP)
        $ pip install -Ur requirements.txt

### Step (3)
#### RUN core.py         
        $ python3 core.py
