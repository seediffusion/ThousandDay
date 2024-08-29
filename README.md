# Thousand Day
***
## Introduction
This simple program calculates your age in days based on your birthday and the current date, and tells you exactly when you will be exactly X thousand days old, as long as how many days remain until that date.
### Note
This program only runs on Windows 7 and higher for now. I can't get a dedicated machine to install Linux on, and any Linux VM I create is laggy as all hell, so sadly, I can't create a Linux version.
***
## Launching
### Uncompiled
1. Ensure that [Python](https://python.org) 3.7 or higher is installed on your system.
2. Press Windows + R, type cmd, and press Enter.
3. Change to the folder with ThousandDay.py in it.

> cd C:\ThousandDay

4. Type the following:

> python ThousandDay.py

If python.exe is not in your MS-DOS path variable, you will have to manually specify the path to the executable, such as C:\python37\python.exe.
### Compiled
Simply navigate to wherever ThousandDay.exe is located, and press enter or double-click to launch the executable. Since the executable is compiled, you don't need Python or anything on your system to run it.
### Copying to clipboard
If you want the calculation automatically copied to the clipboard as well as displayed on screen, type [c] before the date. For example,

> [c]2005-01-01

***
## Privacy
Though this program asks for your date of birth, it will only use this data to calculate your thousand day, and nothing else. Furthermore, the program runs entirely without an internet connection, meaning neither your birthday, your age in days, nor your thousand day are sent to any online locations for processing, usage tracking, advertising, sale to third parties etc. All the information the program uses is stored in your PC's [RAM](https://techterms.com/definition/ram), and is wiped out when the program exits.
***
## Credits
This program is based on the [Thousand Days concept](https://gist.github.com/scruss/3e52ce929b651eedc815baf78df10874) from Stewart Russell, A.K.A. Scruss. [Follow Scruss on Mastodon](https://xoxo.zone/@scruss).