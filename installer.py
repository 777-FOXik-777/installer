#--------------------------------------------------
# ToolName   : Installer
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2022
# Language   : Python
#--------------------------------------------------


import os, time, sys

os.system('clear')

os.system('rm -fr /data/data/com.termux/files/home/setup_installer.py')
os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/updatepak')
os.system('rm -fr README.md')

os.system('clear')


#проверка нахождения Installer


filename = "/data/data/com.termux/files/home/installer"

if os.path.exists(filename):
  os.system('clear')

else:
  os.system('mv setup_installer.py /data/data/com.termux/files/home/')
  os.system('clear')
  print("ВНИМАНИЕ! Запуск не возможен!")
  print("Installer Установлен НЕ в главную папку /home")
  print("")
  print("ЧТОБЫ ИСПРАВИТЬ ОШИБКУ, ВСТАВТЕ КОМАНДУ:")
  print("")
  print("cd && python setup_installer.py")
  print("")
  sys.exit()  






# Установка зависсимсот


print(f'\33]0; Installer ➤ Установка зависимостей...\a',
                  end='', flush=True)




filename = "/data/data/com.termux/files/home/Installer_Files"

if os.path.exists(filename):

  os.system('rm -fr /data/data/com.termux/files/home/installer/Installer_Files')

else:

  filename = "/data/data/com.termux/files/home/installer/Installer_Files"

  if os.path.exists(filename):
    
    os.system('mv Installer_Files /data/data/com.termux/files/home')
    
    os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK')

  else:
    
    os.system('clear')





  

# зависимости


os.system('clear')

filename = "/data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK"

if os.path.exists(filename):
    
    os.system('clear')


else:
      
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
    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка lolcat...")
    res()
    time.sleep(1.5)
    os.system('pip install lolcat')
    os.system('clear')

    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка wget...")
    res()
    time.sleep(1.5)
    os.system('pkg install wget -y')
    os.system('clear')

    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python2...")
    res()
    time.sleep(1.5)
    os.system('pkg install python2 -y')
    os.system('clear')

    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python3...")
    res()
    time.sleep(1.5)
    os.system('pkg install python3 -y')

    #запуск на installer
    os.system("""alias installer='cd ~/installer && python installer.py'""")
    os.system("""sed -i '/alias installer="cd ~\/installer && python installer.py/d' ~/.bashrc""")
    os.system("""sed -i '/printf "\\33\]0; Telegram > @SYPEXHACK\\a"/d' ~/.bashrc""")

  
    os.system('rm -fr tg_SYPEXHACK')
    os.chdir('/data/data/com.termux/files/home/installer')
  
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




print(f'\33]0; Installer ➤ Запуск...\a',
                  end='', flush=True)


# легкий запуск


os.system('clear')

filename = "/data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK"

if os.path.exists(filename):
    
    os.system('clear')


else:
  
    os.system("""echo 'printf "\33]0; Telegram > @SYPEXHACK\a"' >> ~/.bashrc""")
    os.system("""alias installer="cd ~/installer && python installer.py" """)
    os.system("""echo 'alias installer="cd ~/installer && python installer.py"' >> ~/.bashrc""")






#проверка


os.system('clear')
os.system('lolcat /data/data/com.termux/files/home/installer/banner/baner.txt')
print(Fore.WHITE+'', Style.BRIGHT)
print (Fore.YELLOW+" ["+Fore.CYAN+"~"+Fore.YELLOW+"] Проверка целостности файлов...")
time.sleep(0.5)



# доп файлы

os.chdir('/data/data/com.termux/files/home')

filename = "Installer_Files"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует корневая папка!")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка: Installer_Files...")
    time.sleep(1)
    res()
    os.mkdir("/data/data/com.termux/files/home/Installer_Files")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash")
  
    os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

  
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/lochost")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/serveo")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/IP")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/holehe")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/h8mail")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/exiftool")
  
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/Auto")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/sypexhack")
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/update")
    
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файлы УСПЕШНО установлены!")
    time.sleep(2)



#стандарт файлы 

os.chdir('/data/data/com.termux/files/home/installer')

filename = "tool1.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: tool1.py")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: tool1.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/tool1.py 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "tool2.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: tool2.py")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: too2.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/tool2.py 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "tool3.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: tool3.py")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: tool3.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/tool3.py 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "set.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: set.py")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: set.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/set.py 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "version"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: version")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: version...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/version 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)
  

filename = "setup_installer.py"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: setup_installer.py")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: setup_installer.py...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/setup_installer.py 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)

#банер

filename = "banner"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    os.mkdir("/data/data/com.termux/files/home/installer/banner")



os.chdir('/data/data/com.termux/files/home/installer/banner')


filename = "baner.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: baner.txt")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: baner.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banner/baner.txt 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "banerset.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: banerset.txt")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: banerset.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banner/banerset.txt 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "banner1.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: banner1.txt")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: banner1.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banner/banner1.txt 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "banner2.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: banner2.txt")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: banner2.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banner/banner2.txt 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)


filename = "banner3.txt"

if os.path.exists(filename):
    time.sleep(0.1)

else:
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"!"+Fore.YELLOW+"] Отсутствует файл: banner3.txt")
    time.sleep(2)
    print (Style.BRIGHT, Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Установка файла: banner3.txt...")
    time.sleep(1)
    res()
    os.system('wget https://raw.githubusercontent.com/777-FOXik-777/installer/main/banner/banner3.txt 2>&1 | awk "sypexhack {print $1}"')
    print (Style.BRIGHT, Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Файл УСПЕШНО установлен!")
    time.sleep(2)



time.sleep(1)
os.system('clear')
os.system('lolcat /data/data/com.termux/files/home/installer/banner/baner.txt')
print(Fore.WHITE+'', Style.BRIGHT)
print (Fore.GREEN+" ["+Fore.CYAN+"!"+Fore.GREEN+"] Все файлы УСПЕШНО прошли проверку!")
time.sleep(1)





#обновление

os.system('clear')

filename = "/data/data/com.termux/files/home/Installer_Files/trash/update"

if os.path.exists(filename):
  
    os.system('clear')


else:
  
    baner()
    print(Fore.WHITE+'', Style.BRIGHT)
    print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"~"+Fore.YELLOW+"] Проверка наличий обновлений...")
    print(Fore.WHITE+'', Style.BRIGHT)
    time.sleep(1)

    os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
  
    os.system('git clone --depth 1  https://github.com/777-FOXik-777/installer updatepak 2>&1 | awk "sypexhack {print $1}"')

    filename = "updatepak"
    
    if os.path.exists(filename):
    
        def compare_files(file1_path, file2_path):
            with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
                return file1.read() == file2.read()
        
        
      
        file1_path = "/data/data/com.termux/files/home/Installer_Files/trash/updatepak/version"
        file2_path = "/data/data/com.termux/files/home/installer/version"
        
        result = compare_files(file1_path, file2_path)
        
        if result:
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/updatepak')
            baner()
            print(Fore.WHITE+'', Style.BRIGHT)
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Обновлений нет!")
            print(Fore.WHITE+'', Style.BRIGHT)
            tsu = input(' [Нажмите Enter чтобы продолжить]')
            os.system('clear')
        
        else:
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/updatepak')
            baner()
            print(Fore.WHITE+'', Style.BRIGHT)
            print (Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Есть обновление!")
            print(Fore.WHITE+'', Style.BRIGHT)
            print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Обновить Installer?")
            print(Style.RESET_ALL)
            uodate = input(' Выбери пункт [y/n] ➤ ')
            
            if uodate == 'y':
                os.system('rm -fr /data/data/com.termux/files/home/setup_installer.py')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('mv setup_installer.py /data/data/com.termux/files/home/')
                os.system("""sed -i '/^cd ~\/installer && python installer.py/d' ~/.bashrc""")
                os.system('echo "cd ~/ && python setup_installer.py" >> ~/.bashrc')
                print(f'\33]0; Создайте новый сезон!\a',
                        end='', flush=True)  
                while True:
                    os.system('clear')
                    baner()
                    print(Fore.WHITE+'', Style.BRIGHT)
                    print(Style.BRIGHT, Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Перезапустите Termux или создайте новый сезон!")
                    time.sleep(5)
                    print(f'\33]0;  Не используйте старый сезон Installer!\a',
                    end='', flush=True)
                    
            else:
                os.system('clear')

    else:
        os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/updatepak')
        baner()
        print(Fore.WHITE+'', Style.BRIGHT)
        print (Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Не получилось проверить наличий обновлений!")
        print(Fore.WHITE+'', Style.BRIGHT)
        print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Проверьте подключение к интернету")
        print(Fore.WHITE+'', Style.BRIGHT)
        tsu = input(' [Нажмите Enter чтобы продолжить]')
        os.system('clear')

      
#доступ к файлам

os.system('clear')

filename = "/data/data/com.termux/files/home/storage"

if os.path.exists(filename):
  
    os.system('clear')


else:
  
    print ('\n')
    def res():
        print(Style.RESET_ALL)
        
    os.system('clear')
    baner()
    print(Fore.WHITE+'', Style.BRIGHT)
    print (Fore.YELLOW+" ["+Fore.CYAN+"!"+Fore.YELLOW+"] Разрешите доступ к файлам устройства")
    os.system('termux-setup-storage')
    time.sleep(1)
    print(Fore.WHITE+'', Style.BRIGHT)
    tsu = input(' [Нажмите Enter чтобы продолжить]')
    os.system('clear')



#фото


filename = "/data/data/com.termux/files/home/Installer_Files/trash/hack"

if os.path.exists(filename):
  
  filename = "/data/data/com.termux/files/home/storage"
  
  if os.path.exists(filename):

      filename = "/data/data/com.termux/files/home/installer/image/hack.jpg"
  
      if os.path.exists(filename):
      
        os.system('mv /data/data/com.termux/files/home/installer/image/hack.jpg /sdcard/Pictures')
        os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/hack')
        os.system('clear')

      else:
        os.system('clear')
  
  else:
      os.system('clear')

else:
    os.system('clear')



# удаление мусора


os.system('rm -fr /data/data/com.termux/files/home/installer/README.md')
os.system('rm -fr /data/data/com.termux/files/home/installer/image')

filename = "/data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK"

if os.path.exists(filename):
    os.system('clear')

else:
    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK")
    os.system('clear')




#автозапуск после обновления


os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

filename = "Auto"

if os.path.exists(filename):
  
  os.system('clear')

else:

  os.system("""sed -i '/^cd ~\/installer && python installer.py/d' ~/.bashrc""")
  os.system('echo "cd ~/installer && python installer.py" >> ~/.bashrc')





print(Style.RESET_ALL)
os.system('clear')
print(Fore.WHITE+'', Style.BRIGHT)
print("[+]═════════════════════════════════════════════════[+]")
print("")
print("Этот инструмент предназначен только для образовательных")
print("целей. Некоторые утилиты, фото, и прочие файлы взяты из")
print("открытых источников и принадлежат их законным авторам.")
print("")
print("[+]═════════════════════════════════════════════════[+]")
print("")
time.sleep(5)



#разрешание запуск

os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')



os.chdir('/data/data/com.termux/files/home/installer')
os.system('python tool1.py')


#--------------------------------------------------
# ToolName   : Installer
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2022
# Language   : Python
#--------------------------------------------------
