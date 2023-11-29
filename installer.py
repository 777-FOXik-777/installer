import os, time

os.system('clear')

print(f'\33]0; Installer - Установка...\a',
                  end='', flush=True)



os.chdir('/data/data/com.termux/files/home/')

filename = "Installer_Files"

if os.path.exists(filename):
  
  os.chdir('/data/data/com.termux/files/home/installer')
  os.system('rm -fr Installer_Files')
  os.system('clear')

else:

  os.chdir('/data/data/com.termux/files/home/installer')
  os.system('mv Installer_Files /data/data/com.termux/files/home')
  


os.system('clear')

os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

filename = "tg_SYPEXHACK"

if os.path.exists(filename):

    print ('[~] Установка зависимостей... \n')
    time.sleep(2)
    os.system('clear')
       
    #colorama
    print ('[~] Установка colorama... \n')
    time.sleep(1.5)
    os.system('pip install colorama')
    os.system('clear')
      
    #питон

    from colorama import Fore, Style
    
    print ('\n')
    def res():
        print(Style.RESET_ALL)

    
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python2...")
    res()
    time.sleep(1.5)
    os.system('pkg install python2 -y')
    os.system('clear')
    
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python3...")
    res()
    time.sleep(1.5)
    os.system('pkg install python3 -y')
    
    #доступ к файлам
    
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Разрешите доступ к файлам")
    res()
    time.sleep(1.5)
    os.system('termux-setup-storage')
    tsu = input('\n \n[Нажмите enter чтобы продолжить]')
    os.system('clear')


    os.system('rm -fr tg_SYPEXHACK')
    os.chdir('/data/data/com.termux/files/home/installer')
    
    #запуск
    
    os.system('clear')


else:
    from colorama import Fore, Style

    os.chdir('/data/data/com.termux/files/home/installer')
    print(f'\33]0; Installer - Зависимости уже установлены!\a',
                  end='', flush=True)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Все зависимости уже установлены!")
    time.sleep(2)
    os.system('clear')





os.chdir('/data/data/com.termux/files/home/storage')

filename = "storage"

if os.path.exists(filename):
    
    os.system('clear')


else:
    from colorama import Fore, Style

    os.system('clear')
    print (Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Разрешите доступ к файлам")
    res()
    time.sleep(1.5)
    os.system('termux-setup-storage')
    tsu = input('\n \n[Нажмите enter чтобы продолжить]')
    os.system('clear')




os.chdir('/data/data/com.termux/files/home/installer')
print(Style.RESET_ALL)
print(' Этот инструмент предназначен только для образовательных\n целей. Если вы используете Installer для других целей,\n кроме образования, в таких случаях мы не несем\n ответственности. Все утилиты и файлы взяты из открытых\n источников. Утилиты, фото, видео и прочие файлы\n принадлежат их законным авторам.')
time.sleep(2)
os.system('python3 tool.py')
        
