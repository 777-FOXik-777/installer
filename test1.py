import os, time

from colorama import Fore, Style

os.system('rm -fr /data/data/com.termux/files/home/update.py')

os.system('cd /data/data/com.termux/files/home/installer/')
os.system('clear')



def pri():
    print(f'\33]0; Installer - Страница [2]\a',
                      end='', flush=True)

def exit():
    res()
    exit = input('[Нажмите Enter чтобы выйти]')
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('clear')


def res():
    print(Style.RESET_ALL)


def baner():
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    print(Fore.CYAN+'', Style.BRIGHT)
    os.system('lolcat baner.txt')
    res()
    os.chdir('/data/data/com.termux/files/home/Installer_Files')


#начало
    
while True:
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    pri()
    os.system('lolcat banner1.txt')
    inp = input('\n Выбери пункт ➤ ')
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
            print(Style.BRIGHT,Fore.CYAN+" [Ngrok]")
            res()
            print(Fore.GREEN+'  Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_102 = input('  Изменить порт? [y/n] ➤ ')
            if tru_102 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+" [Ngrok]")
                res()
                we_2 = input('  Введите порт ➤ ')
                if we_2 == '':
                    os.system('clear')
                    baner()
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    print(Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(5)
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
            print(Style.BRIGHT,Fore.CYAN+" [Ngrok]")
            res()
            print(Fore.GREEN+'  Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_102 = input('  Изменить порт? [y/n] ➤ ')
            if tru_102 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+" [Ngrok]")
                res()
                we_2 = input('  Введите порт ➤ ')
                if we_2 == '':
                    os.system('clear')
                    baner()
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    print(Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(5)
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
            print(Style.BRIGHT,Fore.CYAN+" [Localhost]")
            res()
            print(Fore.GREEN+'  Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_202 = input('  Изменить порт? [y/n] ➤ ')
            if tru_202 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+" [Localhost]")
                res()
                qw_2 = input('  Введите порт ➤ ')
                if qw_2 == '':
                    os.system('clear')
                    baner()
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    print(Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(5)
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
            print(Style.BRIGHT,Fore.CYAN+" [Localhost]")
            res()
            print(Fore.GREEN+'  Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_202 = input('  Изменить порт? [y/n] ➤ ')
            if tru_202 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+" [Localhost]")
                res()
                qw_2 = input('  Введите порт ➤ ')
                if qw_2 == '':
                    os.system('clear')
                    baner()
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    print(Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(5)
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
            exit()

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
            exit()

    

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
            exit()
            
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
            exit()

  

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
            exit()
            
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
            exit()


    
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
            print(Style.BRIGHT,Fore.CYAN+" [IP-Tracer]")
            res()
            print(Fore.GREEN+'  [1] Пробить свой IP')
            print(Fore.GREEN+'  [2] Пробить чужой IP')
            res()
            print(Fore.YELLOW+'  [e] выход')
            res()
            tru_801 = input('  Выбери пункт ➤ ')
    
            if tru_801 == '1':
                os.system('clear')
                os.system('trace -m')
                exit()
                
            if tru_801 == '2':
                os.system('clear')
                baner()
                res()
                print(Fore.YELLOW+'    Пример IP'+Fore.CYAN+' 33.73.133.137')
                res()
                tsu_802 = input('  Введите IP ➤ ')
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
            print(Style.BRIGHT,Fore.CYAN+" [IP-Tracer]")
            res()
            print(Fore.GREEN+'  [1] Пробить свой IP')
            print(Fore.GREEN+'  [2] Пробить чужой IP')
            res()
            print(Fore.YELLOW+'  [e] выход')
            res()
            tru_801 = input('  Выбери пункт ➤ ')
    
            if tru_801 == '1':
                os.system('clear')
                os.system('trace -m')
                exit()
                
            if tru_801 == '2':
                os.system('clear')
                baner()
                res()
                print(Fore.YELLOW+'  Пример IP'+Fore.CYAN+' 33.73.133.137')
                res()
                tsu_802 = input('  Введите IP ➤ ')
                os.system('clear')
                os.system('trace -t '+tsu_802)
                exit()
    
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
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('python set_test.py')


    
    if inp == '20':
        leave = "2"
        break    


    
    if inp == '30':
        leave = "3"
        break

    
    
    if inp == 'e':
        leave = "e"
        break



if leave == '2':
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('python test2.py')

if leave == '3':
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('python test3.py')

else:
    print(f'\33]0; Installer - Спасибо за использование\a',
          end='', flush=True)
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    os.system('lolcat baner.txt')
    print(Fore.CYAN+'', Style.BRIGHT)
    print(' Спасибо за использование Installer \n')
    os.chdir('/data/data/com.termux/files/home/installer')