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

os.system('cd /data/data/com.termux/files/home/installer/')
os.system('clear')





os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

filename = "sypexhack"

if os.path.exists(filename):
  os.system('clear')
  print("Installer запускается командой: python installer.py")
  print("")
  sys.exit()


else:
  os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/sypexhack")
  os.system('clear')   





def pri():
    print(f'\33]0; Installer ➤ Страница [3]\a',
                      end='', flush=True)

def exit():
    print(Fore.WHITE+'', Style.BRIGHT)
    exit = input(' [Нажмите Enter чтобы закрыть]')
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('clear')


def res():
    print(Style.RESET_ALL)


def baner():
    os.system('clear')
    os.system('lolcat ~/installer/banner/baner.txt')
    res()


#начало
    
while True:
    pri()
    os.system('lolcat ~/installer/banner/banner3.txt')
    inp = input('\n Выбери пункт ➤ ')
    os.system('clear')





    if inp == '21':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "TigerVirus"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] TigerVirus уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('TigerVirus')
            os.system('clear')
            os.system('bash TigerVirus.sh')
            exit()
            
        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] TigerVirus еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка TigerVirus...")
            res()
            os.system('git clone https://github.com/Devil-Tigers/TigerVirus.git')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('TigerVirus')
            os.system('clear')
            os.system('bash TigerVirus.sh')
            exit()

  


  
    if inp == '22':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "hammer"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Hammer уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            baner()
            os.chdir('hammer')
            print(Style.BRIGHT,Fore.CYAN+"[Hammer]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Hammer позволяет задудосить сайт по IP")
            res()
            print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Пример IP:"+Fore.CYAN+" 33.73.133.137")
            res()
            print(Style.BRIGHT,Fore.RED+"[e] Выход")
            res()
            tru_701 = input(' Введите IP ➤ ')
            if tru_701 == 'e':
                os.system('clear')

            else:
                os.system('clear')
                baner()
                os.system('python hammer.py -s '+tru_701+'')
                exit()


        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Hammer еще НЕ установлен!")
            time.sleep(2)
            
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка optparse-pretty...")
            res()
            os.system('pip install optparse-pretty')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка queue...")
            res()
            os.system('pip install queuelib')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Hammer...")
            res()
            os.system('git clone https://github.com/777-oleg-777/hammer')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            baner()
            os.chdir('hammer')
            print(Style.BRIGHT,Fore.CYAN+"[Hammer]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Hammer позволяет задудосить сайт по IP")
            res()
            print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Пример IP:"+Fore.CYAN+" 33.73.133.137")
            res()
            print(Style.BRIGHT,Fore.RED+"[e] Выход")
            res()
            tru_701 = input(' Введите IP ➤ ')
            if tru_701 == 'e':
                os.system('clear')

            else:
                baner()
                os.system('python hammer.py -s '+tru_701+'')
                os.system('clear')
                exit()

  


  
    if inp == '23':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "noisy"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Noisy уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
          
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Noisy]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Noisy позволяет переполнить лог-файлы провайдера")
            res()
            print(Style.BRIGHT,Fore.GREEN+"[y] Запустить")
            res()
            print(Style.BRIGHT,Fore.RED+"[e] Выход")
            res()
            tru_501 = input(' Выбери пункт ➤ ')
            
            if tru_501 == 'y':
                os.chdir('noisy')
                print(Fore.WHITE+'', Style.BRIGHT)
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[Noisy]")
                print(Fore.WHITE+'', Style.BRIGHT)
                print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Закрыть Noisy: Ctrl + C")
                print(Fore.WHITE+'', Style.BRIGHT)
                os.system("python noisy.py --config config.json")
                exit()
    
            else:
                os.system('clear')

        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Noisy еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
            res()
            os.system('pip install requests')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка noisy...")
            res()
            os.system('git clone https://github.com/777-oleg-777/noisy.git')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Noisy]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Noisy позволяет переполнить лог-файлы провайдера")
            res()
            print(Style.BRIGHT,Fore.GREEN+"[y] Запустить")
            res()
            print(Style.BRIGHT,Fore.RED+"[e] Выход")
            res()
            tru_501 = input(' Выбери пункт ➤ ')
            
            if tru_501 == 'y':
                os.chdir('noisy')
                print(Fore.WHITE+'', Style.BRIGHT)
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[Noisy]")
                print(Fore.WHITE+'', Style.BRIGHT)
                print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Закрыть Noisy: Ctrl + C")
                print(Fore.WHITE+'', Style.BRIGHT)
                os.system("python noisy.py --config config.json")
                exit()
    
            else:
                os.system('clear')



  
    
    if inp == '24':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "k-fuscator"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] K-fuscator уже установлен!")
            time.sleep(2)
          
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('k-fuscator')
            os.system('clear')
            os.system('python3 kf.py')
            exit()
            
        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] K-fuscator еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка K-fuscator...")
            res()
            os.system('git clone https://github.com/KasRoudra/k-fuscator.git')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('k-fuscator')
            os.system('clear')
            os.system('python3 kf.py')
            exit()



  

    if inp == '25':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
        filename = "exiftool"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Exiftool еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Exiftool...")
            res()
            os.system('pkg install exiftool -y')
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/exiftool')
            os.system('clear')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Exiftool]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Exiftool позволяет узнать метаданные фото")
            res()
            print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Пример пути:"+Fore.CYAN+" /storage/pictures/example.jpg")
            res()
            print(Style.BRIGHT,Fore.RED+"[e] Выход")
            res()
            tru_250 = input(' Введите путь к фото ➤ ')

            if tru_250 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('exiftool ~'+tru_250+'')
                exit()

        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Exiftool уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Exiftool]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Exiftool позволяет узнать метаданные фото")
            res()
            print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Пример пути:"+Fore.CYAN+" /storage/pictures/example.jpg")
            res()
            print(Style.BRIGHT,Fore.RED+"[e] Выход")
            res()
            tru_250 = input(' Введите путь к фото ➤ ')

            if tru_250 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('exiftool ~'+tru_250+'')
                exit()













    if inp == '26':
        os.system('xdg-open https://github.com/777-FOXik-777')
        os.system('clear')

  
    if inp == '27':
        os.system('xdg-open https://github.com/777-FOXik-777')
        os.system('clear')


    if inp == '28':
        os.system('xdg-open https://github.com/777-FOXik-777')
        os.system('clear')
  

    if inp == '29':
        os.system('xdg-open https://github.com/777-FOXik-777')
        os.system('clear')

  

    
    


    
    if inp == 't':
        os.system('xdg-open https://yoomoney.ru/to/4100117367004233/0')
        os.system('clear')

    
    
    if inp == 's':
        os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('python set.py')


    
    if inp == '10':
        leave = "1"
        break    


    
    if inp == '20':
        leave = "2"
        break

    
    
    if inp == 'e':
        leave = "e"
        break




if leave == '1':
    os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
    os.chdir('/data/data/com.termux/files/home/installer')
    
    lomik = "python tool1.py"

if leave == '2':
    os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
    os.chdir('/data/data/com.termux/files/home/installer')
  
    lomik = "python tool2.py"

if leave == 'e':
    print(f'\33]0; Telegram: @SYPEXHACK желает вам Хорошего дня!\a',
          end='', flush=True)
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    os.system('lolcat baner.txt')
    print(Fore.CYAN+'', Style.BRIGHT)
    print (Fore.YELLOW+" ["+Fore.CYAN+"~"+Fore.YELLOW+"] "+Fore.CYAN+"Telegram: @SYPEXHACK желает вам "+Fore.YELLOW+"Хорошего дня!")
  
    lomik = "echo  "

os.system(""+lomik+"")


#--------------------------------------------------
# ToolName   : Installer
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2022
# Language   : Python
#--------------------------------------------------
