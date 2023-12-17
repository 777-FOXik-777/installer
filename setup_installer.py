import os, time, sys

from colorama import Fore, Style

os.system('clear')


filename = "/data/data/com.termux/files/home/installer/setup_installer.py"

if os.path.exists(filename):
  os.system('clear')
  print("Installer уже установлен!")
  print("")
  print("Installer запускается командой: python installer.py")
  print("")
  sys.exit()


else:
  os.system('clear')   



print(f'\33]0; Installer - Установка...\a',
                  end='', flush=True)


os.system('rm -fr /data/data/com.termux/files/home/installer')
os.system('rm -fr installer')
os.chdir('/data/data/com.termux/files/home/')

print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Installer...")
time.sleep(1.5)
print(Fore.WHITE+"")

os.system('git clone https://github.com/777-FOXik-777/installer')

os.system('rm ~/.bashrc')




os.chdir('/data/data/com.termux/files/home/')

filename = "installer"


if os.path.exists(filename):

  print(f'\33]0; Installer - Успешно установлен!\a',
                  end='', flush=True)

  os.system('rm -fr /data/data/com.termux/files/home/setup_installer.py')
  
  os.system('clear')
  os.system('lolcat ~/installer/banner/baner.txt')
  print(Fore.WHITE+" ")
  print(Style.BRIGHT, Fore.YELLOW+"["+Fore.GREEN+"i"+Fore.YELLOW+"] Installer успешно установлен!")
  print(Fore.WHITE+" ")
  lol = input(' [Нажмите Enter чтобы продолжить]')
  os.chdir('/data/data/com.termux/files/home/installer')
  os.system('clear')
  print(Style.RESET_ALL)
  os.system('python testinstaller.py')
        


else:
  
  print(f'\33]0; Installer - Ошибка во время установки!\a',
                  end='', flush=True)
  os.system('clear')
  print(Fore.YELLOW+" ["+Fore.RED+"!"+Fore.YELLOW+"] Ошибка во время установки Installer!")
  print(Fore.WHITE+" ")
  print(Fore.YELLOW+" ["+Fore.CYAN+"i"+Fore.YELLOW+"] Повторите командой:"+Fore.WHITE+" python setup_installer.py")
  print(Fore.WHITE+" ")
