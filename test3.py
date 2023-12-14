import os, time

from colorama import Fore, Style

os.system('cd /data/data/com.termux/files/home/installer/')
os.system('clear')



def pri():
    print(f'\33]0; Installer - Страница [3]\a',
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
    os.system('lolcat baner.txt')
    res()
    os.chdir('/data/data/com.termux/files/home/Installer_Files')


#начало
    
while True:
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    pri()
    os.system('lolcat banner3.txt')
    inp = input('\n Выбери пункт ➤ ')
    os.system('clear')
    


    if inp == '21':
        os.system('clear')









    
    


    
    if inp == 't':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')

    
    
    if inp == 's':
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('python set_test.py')


    
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
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('python test1.py')

if leave == '2':
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('python test2.py')

else:
    print(f'\33]0; Installer - Спасибо за использование\a',
          end='', flush=True)
    os.chdir('/data/data/com.termux/files/home/installer/banner')
    os.system('clear')
    os.system('lolcat baner.txt')
    print(Fore.CYAN+'', Style.BRIGHT)
    print(' Спасибо за использование Installer \n')
    os.chdir('/data/data/com.termux/files/home/installer')
