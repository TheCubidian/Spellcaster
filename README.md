# Spellcaster
As you traverse your terminal, you come across a script in your filesystem, Spellcaster.py. You curiously start typing:
```bash
python3 Spellcaster.py
```
and push down the Enter key...
***
This is a simple but nevertheless entertaining python game where the aim of the game is to defeat enemies you come across in a command line environment with spells you choose. The effectiveness of your choice is based on the enemy's weakness (and strength) which you are supposed to figure out yourself by common sense and some good ol' trial and error!
***
You can either play it from [here](https://cubidian.me/projects/spellcaster), but that's currently broken because the python backend service I embedded doesnt accept input for the script so I need to find one that does,<br>
**or**<br>
To be able to run this script on your PC, follow this guide:
1. Use your system package manager to install python (it's `python3` here since `python` will install python v2 which has reached end-of-life and frankly shouldn't be used for scripts that were made on and for python v3)
## Windows (Powershell)
```powershell
winget install Python.Python.3
```
## Linux
### Debian-based distributions
e.g. Ubuntu, Raspberry Pi Desktop...
```bash
sudo apt update
sudo apt install python3
```
### Alpine Linux
```bash
sudo apk add python3
```
If you have a different linux distro, i'm going to assume you know how to use your package manager because you would have known what you were doing when you chose your OS (i'm looking at you, arch users!).<br><br>
2. Now to download, follow [this](https://raw.githubusercontent.com/TheCubidian/Spellcaster/main/main.py) link. <br><br>
3. Finally, to run, go the same directory as to where you downloaded it (using `cd <path>`, and run `python3 main.py`. <br><br>
If you don't know how paths work, go into your file manager, right click on the file, and select copy path. If you decide to do it this way, you don't have to use `cd` at all! Youcan just run `python3 </path/you/copied>` and the program will start!
***
A project made with 💜 for Hack Club Scraps
