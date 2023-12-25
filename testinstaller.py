import os, time

os.system('clear')

os.system('rm -fr /data/data/com.termux/files/home/setup_installer.py')

os.system('rm -fr README.md')

os.system('clear')

print(f'\33]0; Installer - Установка...\a',
                  end='', flush=True)





filename = "/data/data/com.termux/files/home/Installer_Files"

if os.path.exists(filename):
  
  os.chdir('/data/data/com.termux/files/home/installer')
  os.system('rm -fr Installer_Files')
  os.system('clear')

else:

  os.chdir('/data/data/com.termux/files/home/installer')
  os.system('mv Installer_Files /data/data/com.termux/files/home')






os.system('clear')

filename = "/data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK"

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
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка lolcat...")
    res()
    time.sleep(1.5)
    os.system('pip install lolcat')
    os.system('clear')

    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка wget...")
    res()
    time.sleep(1.5)
    os.system('pkg install wget -y')
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


    os.system('rm -fr tg_SYPEXHACK')
    os.chdir('/data/data/com.termux/files/home/installer')
    
    os.system('clear')


else:
  
    os.system('clear')



from colorama import Fore, Style

#mef

def res():
        print(Style.RESET_ALL)
  
def baner():
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    os.system('lolcat baner.txt')
    os.chdir('/data/data/com.termux/files/home/Installer_Files')





#проверка


os.system('clear')
os.system('lolcat /data/data/com.termux/files/home/installer/banner/baner.txt')
print (Fore.YELLOW+"\n ["+Fore.CYAN+"~"+Fore.YELLOW+"] Проверка целостности файлов...")
time.sleep(3)

os.chdir('/data/data/com.termux/files/home/installer')

filename = "test1.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: tool1.py")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: tool1.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/test1.py')


filename = "test2.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: tool2.py")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: too2.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/test2.py')


filename = "test3.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: tool3.py")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: tool3.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/test3.py')


filename = "set_test.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: set.py")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: set.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/set_test.py')


filename = "setup_installer.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: setup_installer.py")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: setup_installer.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/setup_installer.py')

#банер

filename = "banner"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    os.mkdir("/data/data/com.termux/files/home/installer/banner")



os.chdir('/data/data/com.termux/files/home/installer/banner')


filename = "banner/baner.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: baner.txt")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: baner.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/baner.txt')


filename = "banner/banerset.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: banerset.txt")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: banerset.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banerset.txt')


filename = "banner/banner1.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: banner1.txt")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: banner1.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banner1.txt')

os.system('clear')
os.system('lolcat /data/data/com.termux/files/home/installer/banner/banner1.txt')
print (Fore.YELLOW+"\n ["+Fore.CYAN+"~"+Fore.YELLOW+"] Все файлы УСПЕШНО прошли проверку!")
time.sleep(3)


filename = "banner/banner2.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: banner2.txt")
    time.sleep(2)
    print (Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: banner2.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banner2.txt')

os.system('clear')
os.system('lolcat /data/data/com.termux/files/home/installer/banner/banner2.txt')
print (Fore.YELLOW+"\n ["+Fore.CYAN+"~"+Fore.YELLOW+"] Все файлы УСПЕШНО прошли проверку!")
time.sleep(3)


os.system('clear')

os.chdir('/data/data/com.termux/files/home')

filename = "storage"

if os.path.exists(filename):
  
    os.system('clear')


else:
  
    print ('\n')
    def res():
        print(Style.RESET_ALL)
        
    os.system('clear')
    baner()
    print (Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Разрешите доступ к файлам")
    res()
    os.system('termux-setup-storage')
    tsu = input(' [Нажмите Enter чтобы продолжить]')
    os.system('clear')



#фото



os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

filename = "hack"

if os.path.exists(filename):

  os.chdir('/data/data/com.termux/files/home')
  
  filename = "storage"
  
  if os.path.exists(filename):
      
      os.system('mv /data/data/com.termux/files/home/installer/image/hack.jpg /sdcard/Pictures')
      os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/hack')
      os.system('clear')
  
  else:
      os.system('clear')

else:
    os.system('clear')






os.system('rm -fr /data/data/com.termux/files/home/installer/README.md')
os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK')
os.system('rm -fr /data/data/com.termux/files/home/installer/image')



#автозапуск после обновления


os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

filename = "Auto"

if os.path.exists(filename):
  
  os.system('clear')

else:

  os.system('echo "cd && cd installer && python tool.py" >> ~/.bashrc')
  os.system('clear')





print(Style.RESET_ALL)
os.system('clear')
print(Fore.WHITE+'', Style.BRIGHT)
print("[+]═════════════════════════════════════════════════[+]")
print("")
print("Этот инструмент предназначен только для образовательных")
print("целей. Все утилиты, фото, видео и прочие и прочие файлы")
print("взяты из открытых источников и принадлежат их законным ")
print("авторам.                                               ")
print("")
print("[+]═════════════════════════════════════════════════[+]")
print("")
time.sleep(5)



#разрешание запуск

os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')



os.chdir('/data/data/com.termux/files/home/installer')
os.system('python test1.py')
