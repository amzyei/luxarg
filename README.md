# luxarg :

![issues](https://img.shields.io/github/issues/amzy-0/luxarg)

![forks](https://img.shields.io/github/forks/amzy-0/luxarg)

![stars](https://img.shields.io/github/stars/amzy-0/luxarg)

![license](https://img.shields.io/github/license/amzy-0/luxarg)


Luxarg is a keyboard-friendly text editor.

The project was started in August 2019 and restarted on June 13 at 20:14:41, 2021.

Easy to use and user-friendly!


# LUXARG support :

![](https://icons.iconarchive.com/icons/igh0zt/ios7-style-metro-ui/72/MetroUI-Folder-OS-Windows-8-icon.png) 
Windows
![](https://icons.iconarchive.com/icons/tatice/operating-systems/48/Fedora-icon.png) 
Fedora
![](https://icons.iconarchive.com/icons/fatcow/farm-fresh/32/centos-icon.png)
CENTOS
![](https://icons.iconarchive.com/icons/saki/nuoveXT/48/Apps-redhat-icon.png)
RedHat
![](https://icons.iconarchive.com/icons/tatice/operating-systems/48/Debian-icon.png)
Debian
![](https://icons.iconarchive.com/icons/tatice/operating-systems/48/Ubuntu-icon.png)
Ubuntu
![](https://icons.iconarchive.com/icons/papirus-team/papirus-apps/48/distributor-logo-opensuse-icon.png)
OpenSUSE
![](https://icons.iconarchive.com/icons/fatcow/farm-fresh/32/arch-linux-icon.png)
Arch
![](https://icons.iconarchive.com/icons/papirus-team/papirus-apps/48/manjaro-welcome-icon.png)
Manjaro

# ICON

![ICON](icon/luxarg.png)


# screenshot :
### 2019
![screenshot](screenshot/1.png)
### 2024
![screenshot](screenshot/2.png)
### Windows Edition (2024)
![screenshot](screenshot/windows.png)


# KEYS : 

    INSERT MODE : <F1>
    SAVE   MODE : <F2>
    OPEN   MODE : <F3>
    HELP   MODE : <F4>
    TERMINAL 	: <F5>
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



# Microsoft Windows installation guide: 

- Access the MS-Windows directory in the LuxarG project.

- Execute the Setup.exe file in the MS-Windows directory. 

- Proceed with the installation using the guided wizard.


# Linux installation

You have to install "pip" before this STEP...   

    $ make 

    
# dependencies
    
    $ pip install -r requirements.txt

# update method (only for system-wide installation)

    $ git pull -ff
    $ git restore . 
    $ make 
    


# For Install pip
*Please check pip.txt file.*


# Local build and execute

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
#### Install dependencies (BY PIP)
        $ pip install -Ur requirements.txt

### Step (3)
#### RUN main.py         
        $ python3 main.py
