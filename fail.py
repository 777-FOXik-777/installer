import os, time, webbrowser, sys

os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <файлы>]')
    print(Fore.GREEN+'')
    print (" _                 _             _   _               ")
    print ("(_)  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print ("| | | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print ("| | | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|_| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[telegram: @SYPEXHACK]                       [v2.4.3]")
    res()
    print (Fore.YELLOW+'    [1] установить php ')
    print (Fore.YELLOW+'    [2] установить ssh ')
    print (Fore.YELLOW+'    [3] установить requests ')
    print (Fore.YELLOW+'    [4] установить lolcat ')
    print (Fore.YELLOW+'    [5] установить proot ')
    print (Fore.YELLOW+'    [6] установить nano ')
    print (Fore.CYAN+"\n                                     ╔═════════════╗")
    print (Fore.CYAN+'    [77] поддержка автора            ║'+Fore.YELLOW+' утилиты'+Fore.CYAN+'[91] ║')
    print (Fore.CYAN+'    [88] тг канал автора             ║'+Fore.YELLOW+' забавы ' +Fore.CYAN+'[92] ║')
    print (Fore.CYAN+'    [99] тех поддержка               ║'+Fore.GREEN +'>файлы<'  +Fore.CYAN+' [93] ║')
    print (Fore.CYAN+'    [00] выход                       ╚═════════════╝')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '91':
        os.system('clear')
        os.system('python3 tool.py')
        

    if inp == '92':
        os.system('clear')
        os.system('python3 zabava.py')


    if inp == '93':
        os.system('clear')


    if inp == '1':
        os.system('pkg install php -y')
        os.system('pkg install php7 -y')
        os.system('clear')

    if inp == '2':
        os.system('pkg install dropbear -y')
        os.system('pkg install openssh -y')
        os.system('clear')


    if inp == '3':
        os.system('pip install requests')
        os.system('clear')

    if inp == '4':
        os.system('pip install lolcat')
        os.system('clear')

    if inp == '5':
        os.system('pkg install proot')
        os.system('clear')

    if inp == '6':
        os.system('pkg install nano')
        os.system('clear')


    if inp == '77':
        os.system('xdg-open https://www.donationalerts.com/r/legends_never_die')


    if inp == '99':    
        os.system('xdg-open https://t.me/MR_FOXik')
        os.system('clear')
        

    if inp == '88':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')


    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        os.system('rm ~/.bashrc')
        os.system('echo "exit" >> ~/.bashrc')
