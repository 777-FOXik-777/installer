import os, time

from colorama import Fore, Style

os.system('clear')


def res():
    print(Style.RESET_ALL)


os.chdir('/data/data/com.termux/files/home')

os.system('wget -O chek https://raw.githubusercontent.com/777-FOXik-777/installer/main/Installer_Files/version')


filename = "/data/data/com.termux/files/home/chek/3.0.0"

if os.path.exists(filename):
  print("Обновелния нету!")

else:
  print("Есть обновление!")
