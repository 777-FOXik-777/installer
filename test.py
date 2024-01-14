import os, time

from colorama import Fore, Style

os.system('clear')


def res():
    print(Style.RESET_ALL)


os.chdir('/data/data/com.termux/files/home/installer/Installer_Files/version/')

os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/Installer_Files/version/3.0.1')


filename = "/data/data/com.termux/files/home/installer/Installer_Files/version/3.0.1"

if os.path.exists(filename):
  print("Есть обновлени!")

else:
  print("Обновелния нету!")
