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
    print(f'\33]0; Installer - Страница [2]\a',
                      end='', flush=True)

def exit():
    res()
    exit = input(' [Нажмите Enter чтобы выйти]')
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('clear')


def res():
    print(Style.RESET_ALL)


def baner():
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    os.system('lolcat baner.txt')
    res()
    os.chdir('/data/data/com.termux/files/home/Installer_Files')


#начало
    
while True:
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    pri()
    os.system('lolcat banner2.txt')
    inp = input('\n Выбери пункт ➤ ')
    os.system('clear')
    

    
    if inp == '11':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "PhoneInfoga"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Phoneinfoga уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            baner()
            os.chdir('/data/data/com.termux/files/home/Installer_Files/PhoneInfoga')
            print(Style.BRIGHT,Fore.CYAN+"[PhoneInfoga]")
            res()
            print(Fore.GREEN+' Введите телефон в формате E164, пример:'+Fore.CYAN+' +3396360XXXX')
            res()
            print(Fore.YELLOW+" [e] Выход")
            res()
            tru_701 = input(' Введите номер ➤ ')
            if tru_701 == 'e':
                os.system('clear')

            else:
                os.system('clear')
                os.system('python phoneinfoga.py -n '+tru_701+'')
                os.system('clear')
                exit()


        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Phoneinfoga еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
            res()
            os.system('pip install requests')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка bs4...")
            res()
            os.system('pip install bs4')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка html5lib...")
            res()
            os.system('pip install html5lib')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка phonenumbers...")
            res()
            os.system('pip install phonenumbers')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка argparse...")
            res()
            os.system('pip install argparse')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка urllib3...")
            res()
            os.system('pip install urllib3')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Phoneinfoga...")
            res()
            os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
            os.chdir('PhoneInfoga')
            os.system('bash phoneinfoga.sh')
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('rm -fr PhoneInfoga')
            os.system('mv /data/data/com.termux/files/home/PhoneInfoga /data/data/com.termux/files/home/Installer_Files')

            baner()
            os.chdir('/data/data/com.termux/files/home/Installer_Files/PhoneInfoga')
            print(Style.BRIGHT,Fore.CYAN+"[Phoneinfoga]")
            res()
            print(Fore.GREEN+' Введите телефон в формате E164, пример:'+Fore.CYAN+' +3396360XXXX')
            res()
            print(Fore.YELLOW+" [e] Выход")
            res()
            tru_701 = input(' Введите номер ➤ ')
            if tru_701 == 'e':
                os.system('clear')

            else:
                os.system('clear')
                os.system('python phoneinfoga.py -n '+tru_701+'')
                os.system('clear')
                exit()



    if inp == '12':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
        filename = "holehe"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Holehe еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Holehe...")
            res()
            os.system('pip3 install holehe')
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/holehe')
            os.system('clear')

            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Holehe]")
            res()
            print(Fore.GREEN+' Введите почту, пример:'+Fore.CYAN+' test@gmail.com')
            res()
            print(Fore.YELLOW+" [e] Выход")
            res()
            tru_801 = input(' Введите почту ➤ ')
            if tru_801 == '':
                os.system('clear')
            
            if tru_801 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('holehe '+tru_801+' --only-used --no-clear')
                exit()

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Holehe уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Holehe]")
            res()
            print(Fore.GREEN+' Введите почту, пример:'+Fore.CYAN+' test@gmail.com')
            res()
            print(Fore.YELLOW+" [e] Выход")
            res()
            tru_801 = input(' Введите почту ➤ ')
            if tru_801 == '':
                os.system('clear')
            
            if tru_801 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('holehe '+tru_801+' --only-used --no-clear')
                exit()



    if inp == '13':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
        filename = "IP"

        if os.path.exists(filename):
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] IP-Tracer еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка IP-Tracer...")
            res()
            time.sleep(1)
            os.system('git clone https://github.com/rajkumardusad/IP-Tracer.git')
            os.chdir('IP-Tracer')
            os.system('bash install')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/IP')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[IP-Tracer]")
            res()
            print(Fore.GREEN+' [1] Пробить свой IP')
            print(Fore.GREEN+' [2] Пробить чужой IP')
            res()
            print(Fore.YELLOW+' [e] выход')
            res()
            tru_801 = input(' Выбери пункт ➤ ')
    
            if tru_801 == '1':
                os.system('clear')
                os.system('trace -m')
                exit()
                
            if tru_801 == '2':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[IP-Tracer]")
                res()
                print(Fore.YELLOW+' Пример IP:'+Fore.CYAN+' 33.73.133.137')
                res()
                tsu_802 = input(' Введите IP ➤ ')
                os.system('clear')
                os.system('trace -t '+tsu_802)
                exit()
    
            else:
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')

        else:
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] IP-Tracer уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[IP-Tracer]")
            res()
            print(Fore.GREEN+' [1] Пробить свой IP')
            print(Fore.GREEN+' [2] Пробить чужой IP')
            res()
            print(Fore.YELLOW+' [e] выход')
            res()
            tru_801 = input(' Выбери пункт ➤ ')
    
            if tru_801 == '1':
                os.system('clear')
                os.system('trace -m')
                exit()
                
            if tru_801 == '2':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[IP-Tracer]")
                res()
                print(Fore.YELLOW+' Пример IP:'+Fore.CYAN+' 33.73.133.137')
                res()
                tsu_802 = input(' Введите IP ➤ ')
                os.system('clear')
                os.system('trace -t '+tsu_802)
                exit()
    
            else:
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')

    

    if inp == '14':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "sherlock"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Sherlock уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('sherlock')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Sherlock]")
            res()
            print(Fore.GREEN+' Введите ник, пример:'+Fore.CYAN+' oleghka')
            res()
            print(Fore.YELLOW+" [e] Выход")
            res()
            tru_901 = input(' Введите ник ➤ ')
            if tru_901 == '':
                os.system('clear')
            
            if tru_901 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('python sherlock '+tru_901+'')
                exit()

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Sherlock еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка tur-repo...")
            res()
            os.system('pkg install tur-repo')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка numpy...")
            res()
            os.system('pkg install python-numpy -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка pandas...")
            res()
            os.system('pkg install python-pandas -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка certifi...")
            res()
            os.system('pip3 install certifi')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка PySocks...")
            res()
            os.system('pip3 install certifi')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
            res()
            os.system('pip3 install requests')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests-futures...")
            res()
            os.system('pip3 install requests-futures')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка stem...")
            res()
            os.system('pip3 install stem')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка torrequest...")
            res()
            os.system('pip3 install torrequest')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка openpyxl...")
            res()
            os.system('pip3 install openpyxl')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка exrex...")
            res()
            os.system('pip3 install exrex')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Sherlok...")
            res()
            os.system('git clone https://github.com/sherlock-project/sherlock.git')
            os.chdir('sherlock')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Sherlock]")
            res()
            print(Fore.GREEN+' Введите ник, пример:'+Fore.CYAN+' oleghka')
            res()
            print(Fore.YELLOW+" [e] Выход")
            res()
            tru_901 = input(' Введите ник ➤ ')
            if tru_901 == '':
                os.system('clear')
            
            if tru_901 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('python sherlock '+tru_901+'')
                exit()

    

    if inp == '15':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "TigerVirus"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] TigerVirus уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('TigerVirus')
            os.system('clear')
            os.system('bash TigerVirus.sh')
            exit()
            
        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] TigerVirus еще НЕ установлен!")
            time.sleep(2)

            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка TigerVirus...")
            res()
            os.system('git clone https://github.com/Devil-Tigers/TigerVirus.git')
            os.chdir('TigerVirus')
            os.system('clear')
            os.system('bash TigerVirus.sh')
            exit()
            

    
    if inp == '16':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "k-fuscator"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] K-fuscator уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('k-fuscator')
            os.system('clear')
            os.system('python3 kf.py')
            exit()
            
        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] K-fuscator еще НЕ установлен!")
            time.sleep(2)

            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка K-fuscator...")
            res()
            os.system('git clone https://github.com/KasRoudra/k-fuscator.git')
            os.chdir('k-fuscator')
            os.system('clear')
            os.system('python3 kf.py')
            exit()


  
    if inp == '17':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "Discord-Nitro-Generator-and-Checker"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Discord-Nitro-Generator уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('Discord-Nitro-Generator-and-Checker')
            os.system('clear')
            os.system('python3 main.py')
            exit()

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Discord-Nitro-Generator еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
            res()
            os.system('pip install requests')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка discord_webhook...")
            res()
            os.system('pip install discord_webhook')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка colored...")
            res()
            os.system('pip install colored')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка numpy...")
            res()
            os.system('pkg install python-numpy -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Discord-Nitro-Generator...")
            res()
            os.system('git clone https://github.com/logicguy1/Discord-Nitro-Generator-and-Checker.git')
            os.chdir('Discord-Nitro-Generator-and-Checker')
            os.system('clear')
            os.system('python3 main.py')
            exit()

    
    
    if inp == '18':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "shorturl"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] ShortUrl уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.system('ShortUrl')
            exit()
        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] ShortUrl еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка ShortUrl...")
            res()
            os.system('git clone https://github.com/htr-tech/shorturl')
            os.chdir('shorturl')
            os.system('clear')
            os.system('bash setup.sh')
            os.system('ShortUrl')
            exit()



    if inp == '19':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "seeker"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Seeker уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('seeker')
            os.system('clear')
            os.system('python seeker.py')
            exit()
        
        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Seeker еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка dropbear...")
            res()
            os.system('pkg install dropbear -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка openssh...")
            res()
            os.system('pkg install openssh -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка php...")
            res()
            os.system('pkg install php -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка php7...")
            res()
            os.system('pkg install php7 -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка psutil...")
            res()
            os.system('pip install psutil')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка packaging...")
            res()
            os.system('pip install packaging')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
            res()
            os.system('pip install requests')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
            res()
            os.system('git clone https://github.com/thewhiteh4t/seeker.git')
            
            os.chdir('seeker')
            os.system('clear')
            os.system('python seeker.py')
            exit()


    


    

    
    if inp == 't':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')

    
    
    if inp == 's':
        os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('python set_test.py')


    
    if inp == '10':
        leave = "1"
        break    


    
    if inp == '30':
        leave = "3"
        break

    
    
    if inp == 'e':
        leave = "e"
        break



if leave == '1':
    os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('python test1.py')

if leave == '3':
    os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('python test3.py')

else:
    print(f'\33]0; Telegram: @SYPEXHACK желает вам Хорошего дня!\a',
          end='', flush=True)
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    os.system('lolcat baner.txt')
    print(Fore.CYAN+'', Style.BRIGHT)
    print(' Telegram: @SYPEXHACK желает вам '+Fore.YELLOW+'Хорошего дня! \n')
    os.chdir('/data/data/com.termux/files/home/installer')
    sys.exit()
