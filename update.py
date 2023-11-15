import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

os.system('cd')

os.system('rm -fr installer')

print(Fore.YELLOW+" ["+Fore.RED+"i"+Fore.YELLOW+"] Обновление/Переустановление Installer...")
time.sleep(1.5)
print(Fore.WHITE+"")

os.system('rm ~/.bashrc')

os.system('git clone https://github.com/777-FOXik-777/installer && cd installer && python tool.py')
