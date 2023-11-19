import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

os.system('rm -fr /data/data/com.termux/files/home/installer')
os.system('rm -fr installer')
os.chdir('/data/data/com.termux/files/home/')

print(Fore.YELLOW+" ["+Fore.RED+"i"+Fore.YELLOW+"] Обновление/Переустановление Installer...")
time.sleep(1.5)
print(Fore.WHITE+"")

os.system('git clone https://github.com/777-FOXik-777/installer && cd installer')

os.system('rm ~/.bashrc')

os.system('python tool.py')
