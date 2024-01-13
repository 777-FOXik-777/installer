import os, time, sys

from colorama import Fore, Style

os.system('rm -fr /data/data/com.termux/files/home/update.py')

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
    print(f'\33]0; Installer - Страница [1]\a',
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
    os.system('lolcat ~/installer/banner/banner1.txt')
    inp = input('\n Выбери пункт ➤ ')
    os.system('clear')
    
        
    if inp == '1':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
        filename = "ngrok"

        if os.path.exists(filename):
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Ngrok еще НЕ установлен!")
            time.sleep(2) 

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка nodejs-lts...")
            res()
            os.system('pkg install nodejs-lts -y')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка ngrok...")
            res()
            os.system('npm install ngrok')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Ngrok...")
            res()
            os.system('npm install ngrok -g')
            we  = '8080'
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/ngrok')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Ngrok]")
            res()
            print(Style.BRIGHT ,Fore.GREEN+'Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Style.BRIGHT ,Fore.YELLOW+"[e] Выход")
            res()
            tru_102 = input(' Изменить порт? [y/n] ➤ ')
            if tru_102 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[Ngrok]")
                res()
                we_2 = input(' Введите порт ➤ ')
                if we_2 == '':
                    os.system('clear')
                    baner()
                    print(Style.BRIGHT ,Fore.YELLOW+'Вы ничего не ввели!')
                    res()
                    print(Style.BRIGHT ,Fore.CYAN+'Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    print(Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(5)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we+' && clear')
                    os.system('clear')
                    
                else:
                    print(Fore.WHITE+'', Style.BRIGHT)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we_2+' && clear')
                    os.system('clear')
    
            if tru_102 == 'n':
                print(Fore.WHITE+'', Style.BRIGHT)
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
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Ngrok уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            we  = '8080'
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Ngrok]")
            res()
            print(Style.BRIGHT ,Fore.GREEN+'Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Style.BRIGHT ,Fore.YELLOW+"[e] Выход")
            res()
            tru_102 = input(' Изменить порт? [y/n] ➤ ')
            if tru_102 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[Ngrok]")
                res()
                we_2 = input(' Введите порт ➤ ')
                if we_2 == '':
                    os.system('clear')
                    baner()
                    print(Style.BRIGHT ,Fore.YELLOW+'Вы ничего не ввели!')
                    res()
                    print(Style.BRIGHT ,Fore.CYAN+'Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    print(Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(5)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we+' && clear')
                    os.system('clear')
                    
                else:
                    print(Fore.WHITE+'', Style.BRIGHT)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ngrok http '+we_2+' && clear')
                    os.system('clear')
    
            if tru_102 == 'n':
                print(Fore.WHITE+'', Style.BRIGHT)
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
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Localhost еще НЕ установлен!")
            time.sleep(2) 

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка dropbear...")
            res()
            os.system('pkg install dropbear -y')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка openssh...")
            res()
            os.system('pkg install openssh -y')
            qw  = '8080'
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/lochost')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Localhost]")
            res()
            print(Style.BRIGHT ,Fore.GREEN+'Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Style.BRIGHT ,Fore.YELLOW+"[e] Выход")
            res()
            tru_202 = input(' Изменить порт? [y/n] ➤ ')
            if tru_202 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT ,Fore.CYAN+"[Localhost]")
                res()
                qw_2 = input(' Введите порт ➤ ')
                if qw_2 == '':
                    os.system('clear')
                    baner()
                    print(Style.BRIGHT ,Fore.YELLOW+'Вы ничего не ввели!')
                    res()
                    print(Style.BRIGHT ,Fore.CYAN+'Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
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
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Localhost уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            qw  = '8080'
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Localhost]")
            res()
            print(Style.BRIGHT ,Fore.GREEN+'Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            print(Style.BRIGHT ,Fore.YELLOW+"[e] Выход")
            res()
            tru_202 = input(' Изменить порт? [y/n] ➤ ')
            if tru_202 == 'y':
                os.system('clear')
                baner()
                print(Style.BRIGHT ,Fore.CYAN+"[Localhost]")
                res()
                qw_2 = input(' Введите порт ➤ ')
                if qw_2 == '':
                    os.system('clear')
                    baner()
                    print(Style.BRIGHT ,Fore.YELLOW+'Вы ничего не ввели!')
                    res()
                    print(Style.BRIGHT ,Fore.CYAN+'Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    print(Fore.YELLOW+"\n ["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(5)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                    os.system('clear')
                    
                else:
                    print(Fore.WHITE+'', Style.BRIGHT)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(1)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run && clear')
                    os.system('clear')
    
            if tru_202 == 'n':
                print(Fore.WHITE+'', Style.BRIGHT)
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
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] PyPhiser уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('PyPhisher')
            os.system('clear')
            os.system('python3 pyphisher.py')
            exit()

        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] PyPhiser еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка PyPhiser...")
            res()
            os.system('git clone https://github.com/KasRoudra/PyPhisher')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('PyPhisher')
            os.system('clear')
            os.system('python3 pyphisher.py')
            exit()

    

    if inp == '4':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "zphisher"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Zphiser уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('zphisher')
            os.system('clear')
            os.system('bash zphisher.sh')
            exit()
            
        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Zphiser еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Zphiser...")
            res()
            os.system('git clone https://github.com/htr-tech/zphisher')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('zphisher')
            os.system('clear')
            os.system('bash zphisher.sh')
            exit()



    if inp == '5':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "CamHacker"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] CamHacker уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('CamHacker')
            os.system('clear')
            os.system('bash ch.sh')
            res()
            exit()

        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] CamHacker еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка php...")
            res()
            os.system('pkg install php -y')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка CamHacker...")
            res()
            os.system('git clone https://github.com/KasRoudra/CamHacker')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('CamHacker')
            os.system('clear')
            os.system('bash ch.sh')
            exit()



    if inp == '6':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "VidPhisher"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] VidPhisher уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('VidPhisher')
            os.system('clear')
            os.system('bash vp.sh')
            exit()

        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] VidPhisher еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка php...")
            res()
            os.system('pkg install php -y')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка VidPhisher...")
            res()
            os.system('git clone https://github.com/KasRoudra/VidPhisher')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('VidPhisher')
            os.system('clear')
            os.system('bash vp.sh')
            exit()



    if inp == '7':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "Telephish"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Telephish уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('Telephish')
            os.system('clear')
            os.system('python builder.py')
            os.system('clear')
            baner()
            os.system('python Instagram.py')
            os.system('clear')
            baner()
            os.system('python vk.py')
            os.system('clear')
            baner()
            os.system('python tiktok.py')
            os.system('rm -fr Instagram.py')
            os.system('rm -fr vk.py.py')
            os.system('rm -fr tiktok.py')
            os.system('clear')
            exit()

        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Telephish еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка pyTelegramBotAPI...")
            res()
            os.system('pip install pyTelegramBotAPI')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Telephish...")
            res()
            os.system('git clone https://github.com/lamer112311/Telephish')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('Telephish')
          
            os.system('clear')
            os.system('python builder.py')
            os.system('clear')
            baner()
            os.system('python Instagram.py')
            os.system('clear')
            baner()
            os.system('python vk.py')
            os.system('clear')
            baner()
            os.system('python tiktok.py')
            os.system('rm -fr Instagram.py')
            os.system('rm -fr vk.py.py')
            os.system('rm -fr tiktok.py')
            os.system('clear')
            exit()



    if inp == '8':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "Dnnme2"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Dnnme2 уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('Dnnme2')
            os.system('clear')
            os.system('python build.py')
            os.system('clear')
            baner()
            os.system('python probiv.py')
            os.system('clear')
            baner()
            os.system('python nacr.py')
            os.system('clear')
            baner()
            os.system('python brawl.py')
            os.system('clear')
            baner()
            os.system('python znak.py')
            os.system('clear')
            baner()
            os.system('python btc.py')
            os.system('rm -fr nacr.py')
            os.system('rm -fr probiv.py')
            os.system('rm -fr brawl.py')
            os.system('rm -fr znak.py')
            os.system('rm -fr btc.py')
            os.system('clear')
            exit()

        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Dnnme2 еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка pyTelegramBotAPI...")
            res()
            os.system('pip install pyTelegramBotAPI')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Dnnme2...")
            res()
            os.system('git clone https://github.com/lamer112311/Dnnme2')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('Dnnme2')
          
            os.system('clear')
            os.system('python build.py')
            os.system('clear')
            baner()
            os.system('python probiv.py')
            os.system('clear')
            baner()
            os.system('python nacr.py')
            os.system('clear')
            baner()
            os.system('python brawl.py')
            os.system('clear')
            baner()
            os.system('python znak.py')
            os.system('clear')
            baner()
            os.system('python btc.py')
            os.system('rm -fr nacr.py')
            os.system('rm -fr probiv.py')
            os.system('rm -fr brawl.py')
            os.system('rm -fr znak.py')
            os.system('rm -fr btc.py')
            os.system('clear')
            exit()



    if inp == '9':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "maskphish"

        if os.path.exists(filename):
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"!"+Fore.YELLOW+"] Maskphish уже установлен!")
            time.sleep(2)
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            
            os.chdir('maskphish')
            os.system('clear')
            os.system('bash maskphish.sh')
            exit()
            
        else:
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Maskphish еще НЕ установлен!")
            time.sleep(2)

            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Maskphish...")
            res()
            os.system('git clone https://github.com/jaykali/maskphish.git')
            print(Fore.WHITE+'', Style.BRIGHT)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)
            os.chdir('maskphish')
            os.system('clear')
            os.system('bash maskphish.sh')
            exit()


    




  

    if inp == 't':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')

    
    
    if inp == 's':
        os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
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
    os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
    os.chdir('/data/data/com.termux/files/home/installer')
    
    lomik = "python test2.py"

if leave == '3':
    os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/sypexhack')
    os.chdir('/data/data/com.termux/files/home/installer')
  
    lomik = "python test3.py"

if leave == 'e':
    print(f'\33]0; Telegram: @SYPEXHACK желает вам Хорошего дня!\a',
          end='', flush=True)
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    os.system('lolcat baner.txt')
    print(Fore.CYAN+'', Style.BRIGHT)
    print(' Telegram: @SYPEXHACK желает вам '+Fore.YELLOW+'Хорошего дня!')
  
    lomik = "echo  "

os.system(""+lomik+"")
