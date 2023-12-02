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
  print(Fore.YELLOW+" ["+Fore.GREEN+"i"+Fore.YELLOW+"] Installer успешно установлен!")
  print(Fore.WHITE+" ")
  tsu = input(' [Нажмите Enter чтобы продолжить]')
  os.chdir('/data/data/com.termux/files/home/installer')
  os.system('clear')
  print(Style.RESET_ALL)
  print(' Этот инструмент предназначен только для образовательных\n целей. Если вы используете Installer для других целей,\n кроме образования, в таких случаях мы не несем\n ответственности. Все утилиты, фото, видео и прочие файлы\n взяты из открытых источников\n и принадлежат их законным авторам.')
  time.sleep(2)
  os.system('python3 tool.py')
        


else:
  
  print(f'\33]0; Installer - Ошибка во время обновления!\a',
                  end='', flush=True)
  os.system('clear')
  print(Fore.YELLOW+" ["+Fore.RED+"!"+Fore.YELLOW+"] Ошибка во время установки Installer!")
  print(Fore.WHITE+" ")
  print(Fore.YELLOW+" ["+Fore.GREEN+"i"+Fore.YELLOW+"] Повторите используя команду:"+Fore.WHITE+" python update.py")
  print(Fore.WHITE+" ")
