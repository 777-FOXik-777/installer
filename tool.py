import os, time

from colorama import Fore, Style

os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/tg_SYPEXHACK')
os.system('rm -fr /data/data/com.termux/files/home/update.py')




os.chdir('/data/data/com.termux/files/home')

filename = "storage"

if os.path.exists(filename):

    os.system('mv /data/data/com.termux/files/home/installer/image/hack.jpg /sdcard/Pictures')
    os.system('rm -fr /data/data/com.termux/files/home/installer/image')
    os.system('clear')


else:
    from colorama import Fore, Style

    print ('\n')
    def res():
        print(Style.RESET_ALL)
        
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Разрешите доступ к файлам")
    res()
    time.sleep(1.5)
    os.system('termux-setup-storage')
    tsu = input('\n[Нажмите Enter чтобы продолжить]')
    os.system('clear')





print(Style.RESET_ALL)
print(' Этот инструмент предназначен только для образовательных\n целей. Если вы используете Installer для других целей,\n кроме образования, в таких случаях мы не несем\n ответственности. Все утилиты, фото, видео и прочие\n файлы взяты из открытых источников и принадлежат\n их законным авторам.')
time.sleep(2)



os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

filename = "Auto"

if os.path.exists(filename):
  
  os.system('clear')

else:

  os.system('echo "cd && cd installer && python tool.py" >> ~/.bashrc')
  os.system('clear')


def pri():
    print(f'\33]0; Installer - Страница [1]\a',
                      end='', flush=True)

def res():
    print(Style.RESET_ALL)

def baner():
    os.system('clear')
    print(Fore.CYAN+'', Style.BRIGHT)
    print("  ___                 _             _   _               ")
    print(" |_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print("  | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print("  | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print(" |___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    res()
    
while True:
    os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
    
    filename = "ngrok"
    if os.path.exists(filename):
      Ngrok = ""+Fore.RED+"X"
    else:
      Ngrok = ""+Fore.GREEN+"✓"
    
    filename = "lochost"
    if os.path.exists(filename):
      Localhost = ""+Fore.RED+"X"
    else:
      Localhost = ""+Fore.GREEN+"✓"
    
    filename = "IP"
    if os.path.exists(filename):
      IPTracer = ""+Fore.RED+"X"
    else:
      IPTracer = ""+Fore.GREEN+"✓"
    
    
    os.chdir('/data/data/com.termux/files/home/Installer_Files')
    
    filename = "PyPhisher"
    if os.path.exists(filename):
      PyPhisher = ""+Fore.GREEN+"✓"
    else:
      PyPhisher = ""+Fore.RED+"X"
    
    filename = "zphisher"
    if os.path.exists(filename):
      Zphisher = ""+Fore.GREEN+"✓"
    else:
      Zphisher = ""+Fore.RED+"X"
    
    filename = "k-fuscator"
    if os.path.exists(filename):
      Kfuscator = ""+Fore.GREEN+"✓"
    else:
      Kfuscator = ""+Fore.RED+"X"
    
    filename = "TigerVirus"
    if os.path.exists(filename):
      TigerVirus = ""+Fore.GREEN+"✓"
    else:
      TigerVirus = ""+Fore.RED+"X"
    
    filename = "maskphish"
    if os.path.exists(filename):
      Maskphish = ""+Fore.GREEN+"✓"
    else:
      Maskphish = ""+Fore.RED+"X"
    
    filename = "seeker"
    if os.path.exists(filename):
      Seeker = ""+Fore.GREEN+"✓"
    else:
      Seeker = ""+Fore.RED+"X"

    os.chdir('/data/data/com.termux/files/home/installer')
    pri()
    baner()
    print(Style.BRIGHT, Fore.CYAN+"[Telegram: @SYPEXHACK]                         ["+Fore.YELLOW+"2.10.1"+Fore.CYAN+"]")
    res()
    print(Fore.GREEN+"    [1] Ngrok      ("+Ngrok+""+Fore.GREEN+")  >>  Тунелирование")
    print(Fore.GREEN+"    [2] Localhost  ("+Localhost+""+Fore.GREEN+")  >>  Тунелирование")
    print(Fore.GREEN+"    [3] PyPhiser   ("+PyPhisher+""+Fore.GREEN+")  >>  Фишинг")
    print(Fore.GREEN+"    [4] Zphisher   ("+Zphisher+""+Fore.GREEN+")  >>  Фишинг")
    print(Fore.GREEN+"    [5] K-fuscator ("+Kfuscator+""+Fore.GREEN+")  >>  Зашифровать код")
    print(Fore.GREEN+"    [6] TigerVirus ("+TigerVirus+""+Fore.GREEN+")  >>  Вирусы apk")
    print(Fore.GREEN+"    [7] Maskphish  ("+Maskphish+""+Fore.GREEN+")  >>  Замаскировать ссылку")
    print(Fore.GREEN+"    [8] IP-Tracer  ("+IPTracer+""+Fore.GREEN+")  >>  Пробив по IP")
    print(Fore.GREEN+"    [9] Seeker     ("+Seeker+""+Fore.GREEN+")  >>  Узнать местоположения")
    res()
    print(Style.BRIGHT,Fore.CYAN+"   "+Fore.YELLOW+"[00] Стр. (1) "+Fore.CYAN+"[10] Стр. (2) "+Fore.CYAN+"[20] Стр. (3)")
    res()
    print(Fore.YELLOW+"    [s] Настройки")
    print(Fore.YELLOW+"    [e] Выход")
    res()
    inp = input(' Выбери пункт>>> ')
    os.system('clear')

    
        
    if inp == '1':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
        filename = "ngrok"

        if os.path.exists(filename):
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Ngrok еще НЕ установлен!")
            time.sleep(2) 
            
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Nodejs-lts...")
            res()
            os.system('pkg install nodejs-lts -y')
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Ngrok...")
            res()
            os.system('npm install ngrok')
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Ngrok...")
            res()
            os.system('npm install ngrok -g')
            we  = '8080'
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/ngrok')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"\n  [Ngrok]")
            res()
            print(Fore.GREEN+'    Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"    [e] Выход")
            res()
            tru_102 = input('  Изменить порт? [y/n] >>> ')
            if tru_102 == 'y':
                os.system('clear')
                baner()
                res()
                we_2 = input('  Введите порт>>> ')
                if we_2 == '':
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    time.sleep(7)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we+' && clear')
                    os.system('clear')
                    
                else:
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we_2+' && clear')
                    os.system('clear')
    
            if tru_102 == 'n':
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                os.system('ngrok http '+we+' && clear')
                os.system('clear')
                
            else:
                os.system('clear')

        else:
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Ngrok уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            we  = '8080'
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"\n  [Ngrok]")
            res()
            print(Fore.GREEN+'    Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"    [e] Выход")
            res()
            tru_102 = input('  Изменить порт? [y/n] >>> ')
            if tru_102 == 'y':
                os.system('clear')
                baner()
                res()
                we_2 = input('  Введите порт>>> ')
                if we_2 == '':
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    time.sleep(7)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we+' && clear')
                    os.system('clear')
                    
                else:
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we_2+' && clear')
                    os.system('clear')
    
            if tru_102 == 'n':
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                os.system('ngrok http '+we+' && clear')
                os.system('clear')
                
            else:
                os.system('clear')


    
    if inp == '2':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
        filename = "lochost"

        if os.path.exists(filename):
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Localhost еще НЕ установлен!")
            time.sleep(2) 

            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка dropbear...")
            res()
            os.system('pkg install dropbear -y')
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка openssh...")
            res()
            os.system('pkg install openssh -y')
            qw  = '8080'
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/lochost')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"\n  [Localhost]")
            res()
            print(Fore.GREEN+'    Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"    [e] Выход")
            res()
            tru_202 = input('  Изменить порт? [y/n] >>> ')
            if tru_202 == 'y':
                os.system('clear')
                baner()
                res()
                qw_2 = input('  Введите порт>>> ')
                if qw_2 == '':
                    os.system('clear')
                    print('\n')
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    time.sleep(7)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                    os.system('clear')
                    
                else:
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run && clear')
                    os.system('clear')
    
            if tru_202 == 'n':
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                os.system('clear')
                
            else:
                os.system('clear')
                
        else:
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Localhost уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            qw  = '8080'
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"\n  [Localhost]")
            res()
            print(Fore.GREEN+'    Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"    [e] Выход")
            res()
            tru_202 = input('  Изменить порт? [y/n] >>> ')
            if tru_202 == 'y':
                os.system('clear')
                baner()
                res()
                qw_2 = input('  Введите порт>>> ')
                if qw_2 == '':
                    os.system('clear')
                    print('\n')
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    time.sleep(7)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                    os.system('clear')
                    
                else:
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run && clear')
                    os.system('clear')
    
            if tru_202 == 'n':
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                os.system('clear')
                
            else:
                os.system('clear')
                
    

    if inp == '3':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "PyPhisher"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] PyPhiser уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('PyPhisher')
            os.system('clear')
            os.system('python3 pyphisher.py')
            res()
            tsu_302 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] PyPhiser еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка PyPhiser...")
            res()
            os.system('git clone https://github.com/KasRoudra/PyPhisher')
            os.chdir('PyPhisher')
            os.system('clear')
            os.system('python3 pyphisher.py')
            res()
            tsu_302 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

    

    if inp == '4':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "zphisher"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Zphiser уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('zphisher')
            os.system('clear')
            os.system('bash zphisher.sh')
            res()
            tsu_401 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
            
        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Zphiser еще НЕ установлен!")
            time.sleep(2)
        
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Zphiser...")
            res()
            os.system('git clone https://github.com/htr-tech/zphisher')
            os.chdir('zphisher')
            os.system('clear')
            os.system('bash zphisher.sh')
            res()
            tsu_401 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

  

    if inp == '5':
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
            res()
            tsu_601 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
            
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
            res()
            tsu_501 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



    
    if inp == '6':
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
            res()
            tsu_601 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
            
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
            res()
            tsu_601 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

    

    if inp == '7':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "maskphish"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Maskphish уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('maskphish')
            os.system('clear')
            os.system('bash maskphish.sh')
            res()
            tsu_701 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
            
        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Maskphish еще НЕ установлен!")
            time.sleep(2)

            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Maskphish...")
            res()
            os.system('git clone https://github.com/jaykali/maskphish.git')
            os.chdir('maskphish')
            os.system('clear')
            os.system('bash maskphish.sh')
            res()
            tsu_701 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')


    
    if inp == '8':
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
            print(Style.BRIGHT,Fore.CYAN+"\n    [IP-Tracer]")
            res()
            print(Fore.GREEN+'    [1] Пробить свой IP')
            print(Fore.GREEN+'    [2] Пробить чужой IP')
            res()
            print(Fore.YELLOW+'    [e] выход')
            res()
            tru_801 = input('  Выбери пункт>>> ')
    
            if tru_801 == '1':
                os.system('clear')
                os.system('trace -m')
                tsu_803 = input('\n [Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')
                
            if tru_801 == '2':
                os.system('clear')
                baner()
                res()
                print(Fore.YELLOW+'    Пример IP'+Fore.CYAN+' 33.73.133.137')
                res()
                tsu_802 = input('  Введите IP >>> ')
                os.system('clear')
                os.system('trace -t '+tsu_802)
                res()
                tsu_804 = input(' [Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')
    
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
            print(Style.BRIGHT,Fore.CYAN+"\n    [IP-Tracer]")
            res()
            print(Fore.GREEN+'    [1] Пробить свой IP')
            print(Fore.GREEN+'    [2] Пробить чужой IP')
            res()
            print(Fore.YELLOW+'    [e] выход')
            res()
            tru_801 = input('  Выбери пункт>>> ')
    
            if tru_801 == '1':
                os.system('clear')
                os.system('trace -m')
                tsu_803 = input('\n [Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')
                
            if tru_801 == '2':
                os.system('clear')
                baner()
                res()
                print(Fore.YELLOW+'    Пример IP'+Fore.CYAN+' 33.73.133.137')
                res()
                tsu_802 = input('  Введите IP >>> ')
                os.system('clear')
                os.system('trace -t '+tsu_802)
                res()
                tsu_804 = input(' [Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')
    
            else:
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')



    if inp == '9':
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
            res()
            tsu_901 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
        
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
            os.system('pkg install php7')
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
            res()
            tsu_901 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')


    

    if inp == '20':
        print(f'\33]0; Installer - Страница [3]\a',
                      end='', flush=True)
        baner()
        print (Fore.YELLOW+" ["+Fore.RED+"!"+Fore.YELLOW+"] Страница (3) еще не доступна!")
        res()
        print(Fore.CYAN+'    [1]'+Fore.CYAN+' Добавить утилиту в Installer')
        res()
        print(Fore.YELLOW+'    [e]'+Fore.YELLOW+' Выход')
        res()
        tsu_20 = input('  Выбери пункт>>> ')

        if tsu_20 == '1':
            os.system('xdg-open https://forms.gle/vMHny8Yp24HQZqLV9')
            os.system('clear')

        else:
            os.system('clear')

    
    
    if inp == '10':
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('python tool2.py')


    
    if inp == 's':
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('clear')
        os.system('python set.py')

    

    if inp == 'e':
        print(f'\33]0; Installer - Спасибо за использование\a',
                      end='', flush=True)
        os.system('cd /data/data/com.termux/files/home/')
        os.system('clear')
        print('\n')
        print(Fore.CYAN+'Спасибо за использование Installer')
        res()
        break
