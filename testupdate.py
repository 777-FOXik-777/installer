import os, time

from colorama import Fore, Style

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

filename = "installer"



if os.path.exists(filename):


  
  os.chdir('/data/data/com.termux/files/home/')

  filename = "Installer_Files"
  
  if os.path.exists(filename):
    
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('rm -fr Installer_Files')
    os.system('clear')

  
  else:
  
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('mv Installer_Files /data/data/com.termux/files/home')

  
  
  print(f'\33]0; Installer - Успешно установлен!\a',
                  end='', flush=True)

  
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
  print(Fore.YELLOW+" ["+Fore.GREEN+"i"+Fore.YELLOW+"] Повторите используя команду:"+Fore.WHITE+" python update.py")
  print(Fore.WHITE+" ")
