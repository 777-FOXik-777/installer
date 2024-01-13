import os, time, sys

from colorama import Fore, Style

os.system('rm -fr /data/data/com.termux/files/home/update.py')

os.system('cd /data/data/com.termux/files/home/installer/')
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


    if inp == '12':
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
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/lochost')
          
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Localhost]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Localhost позволяет туннелировать трафик")
            res()
            print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Пример порта:"+Fore.CYAN+" 8080")
            res()
            print(Style.BRIGHT,Fore.YELLOW+"[e] Выход")
            res()
            tru_201 = input(' Введите порт ➤ ')
            
            if tru_201 == 'e':
                os.system('clear')
          
            else:
                print(Fore.WHITE+'', Style.BRIGHT)
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[Localhost]")
                print(Fore.WHITE+'', Style.BRIGHT)
                print(Fore.YELLOW+" ["+Fore.RED+"~"+Fore.YELLOW+"] Ваша ссылка:"+Fore.WHITE+"")
                res()
                os.system("""ssh -R 80:localhost:"""+tru_201+""" nokey@localhost.run -T -n 2>&1 | awk '/.lhr.life/ {print $6}'""")
                exit()

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

            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"[Localhost]")
            res()
            print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Localhost позволяет туннелировать трафик")
            res()
            print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Пример порта:"+Fore.CYAN+" 8080")
            res()
            print(Style.BRIGHT,Fore.YELLOW+"[e] Выход")
            res()
            tru_201 = input(' Введите порт ➤ ')
            
            if tru_201 == 'e':
                os.system('clear')
          
            else:
                print(Fore.WHITE+'', Style.BRIGHT)
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(1)
                os.system('clear')
                baner()
                print(Style.BRIGHT,Fore.CYAN+"[Localhost]")
                print(Fore.WHITE+'', Style.BRIGHT)
                print(Fore.YELLOW+" ["+Fore.RED+"~"+Fore.YELLOW+"] Ваша ссылка:"+Fore.WHITE+"")
                res()
                os.system("""ssh -R 80:localhost:"""+tru_201+""" nokey@localhost.run -T -n 2>&1 | awk '/.lhr.life/ {print $6}'""")
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
