import os, time

from colorama import Fore, Style

os.system('clear')

print(f'\33]0; Installer update\a',
                  end='', flush=True)

os.system('rm -fr /data/data/com.termux/files/home/installer')
os.system('rm -fr installer')
os.chdir('/data/data/com.termux/files/home/')

print(Fore.YELLOW+" ["+Fore.RED+"i"+Fore.YELLOW+"] Обновление/Переустановка Installer...")
time.sleep(1.5)
print(Fore.WHITE+"")

os.system('git clone https://github.com/777-FOXik-777/installer')

filename = "installer"

if os.path.exists(filename):
  
  os.system('rm ~/.bashrc')
  os.system('clear')
  print(Fore.YELLOW+" ["+Fore.GREEN+"i"+Fore.YELLOW+"] Installer успешно обновлен/переустановлен!")
  print(Fore.WHITE+" ")
  tsu = input(' [Нажмите enter чтобы продолжить]')
  os.system('clear')
  os.system('cd installer && python tool.py')


else:
  
  print(f'\33]0; Installer ошибка во время обновления!\a',
                  end='', flush=True)
  os.system('clear')
  print(Fore.YELLOW+" ["+Fore.RED+"!"+Fore.YELLOW+"] Ошибка во время обновления Installer!")
  print(Fore.WHITE+" ")
  print(Fore.YELLOW+" ["+Fore.GREEN+"i"+Fore.YELLOW+"] Создайте новый сезон в Termux чтобы повторить!")
  print(Fore.WHITE+" ")
