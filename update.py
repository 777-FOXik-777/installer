import os, time

from colorama import Fore, Style

os.system('clear')

print(f'\33]0; Installer установка...\a',
                  end='', flush=True)

os.system('rm -fr /data/data/com.termux/files/home/installer')
os.system('rm -fr installer')
os.chdir('/data/data/com.termux/files/home/')

print(Fore.YELLOW+" ["+Fore.RED+"i"+Fore.YELLOW+"] Обновление/Переустановка Installer...")
time.sleep(1.5)
print(Fore.WHITE+"")

os.system('git clone https://github.com/777-FOXik-777/installer')

os.system('rm ~/.bashrc')

filename = "installer"

if os.path.exists(filename):
  
  print(f'\33]0; Installer - Успешно установлен!\a',
                  end='', flush=True)
  os.system('clear')
  print(Fore.YELLOW+" ["+Fore.GREEN+"i"+Fore.YELLOW+"] Installer успешно обновлен/переустановлен!")
  print(Fore.WHITE+" ")
  tsu = input(' [Нажмите enter чтобы продолжить]')
  os.system('clear')
  os.system('cd installer && python tool.py')


else:
  
  print(f'\33]0; Installer - Ошибка во время обновления!\a',
                  end='', flush=True)
  os.system('clear')
  print(Fore.YELLOW+" ["+Fore.RED+"!"+Fore.YELLOW+"] Ошибка во время обновления Installer!")
  print(Fore.WHITE+" ")
  print(Fore.YELLOW+" ["+Fore.GREEN+"i"+Fore.YELLOW+"] Чтобы повторить используйте команду "+Fore.WHITE+"python update.py "+Fore.YELLOW+"!")
  print(Fore.WHITE+" ")
