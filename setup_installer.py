#--------------------------------------------------
# ToolName   : Installer
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2022
# Language   : Python
#--------------------------------------------------


import os, time, sys

from colorama import Fore, Style

os.system('clear')

#нельзя менять
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



print(f'\33]0; Installer ➤ Установка...\a',
                  end='', flush=True)

os.system('rm -fr /data/data/com.termux/files/home/installer')
os.system('rm -fr installer')
os.chdir('/data/data/com.termux/files/home/')

print(Fore.WHITE+'', Style.BRIGHT)
os.system('clear')
print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Installer...")
time.sleep(1.5)
print(Style.RESET_ALL)

os.system('git clone https://github.com/777-FOXik-777/installer')





os.system("""sed -i '/rm -fr \/data\/data\/com\.termux\/files\/home\/Installer_Files/d' ~/.bashrc""")
os.system("""sed -i '/cd ~\/ && python setup_installer.py/d' ~/.bashrc""")

os.system("""sed -i '/alias installer="cd ~\/installer && python installer.py/d' ~/.bashrc""")
os.system("""echo 'alias installer="cd ~/installer && python installer.py"' >> ~/.bashrc""")


os.system("""sed -i '/printf "\\33\]0; Telegram > @SYPEXHACK\\a"/d' ~/.bashrc""")
os.system("""echo 'printf "\33]0; Telegram > @SYPEXHACK\a"' >> ~/.bashrc""")



os.chdir('/data/data/com.termux/files/home/')

filename = "installer"


if os.path.exists(filename):

  print(f'\33]0; Installer - Успешно установлен!\a',
                  end='', flush=True)

  os.system('rm -fr /data/data/com.termux/files/home/setup_installer.py')
  
  os.system('clear')
  os.system('lolcat ~/installer/banner/baner.txt')
  print(Fore.WHITE+" ")
  print(Style.BRIGHT, Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Installer успешно установлен!")
  print(Fore.WHITE+'', Style.BRIGHT)
  lol = input(' [Нажмите Enter чтобы продолжить]')
  os.chdir('/data/data/com.termux/files/home/installer')
  os.system('clear')
  print(Style.RESET_ALL)
  os.system('python installer.py')
        


else:
  
  print(f'\33]0; Installer - Ошибка во время установки!\a',
                  end='', flush=True)
  os.system('clear')
  print(Style.BRIGHT ,Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Ошибка во время установки Installer!")
  print(Fore.WHITE+" ")
  print(Style.BRIGHT ,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Повторите командой:"+Fore.WHITE+" python setup_installer.py")
  print(Fore.WHITE+" ")


  

#--------------------------------------------------
# ToolName   : Installer
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2022
# Language   : Python
#--------------------------------------------------
