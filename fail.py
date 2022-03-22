import os, time, webbrowser

we = '❌'


    
os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <файлы>]')
    print('\n')
    print(Fore.GREEN+'')
    print (" #                 #          ##    ##              ")
    print ("                   #           #     #              ")
    print ("##   ###    ###   ###    ###   #     #     ##   ### ")
    print (" #   #  #  ##      #    #  #   #     #    # ##  #  #")
    print (" #   #  #    ##    #    # ##   #     #    ##    #   ")
    print ("###  #  #  ###      ##   # #  ###   ###    ##   #   ")
    print ('\n')
    print ("[telegram: @SYPEXHACK]                      [v1.7.5]")
    res()
    time.sleep(1)
    print ('\n')
    print (Fore.YELLOW+'    [1] установить php ['+we)
    print (Fore.YELLOW+"    [2] ")
    print (Fore.YELLOW+"    [3] ")
    print (Fore.YELLOW+"    [4] ")
    print (Fore.YELLOW+"    [5] ")
    print (Fore.YELLOW+"    [6] ")
    print (Fore.YELLOW+"    [7] ")
    print (Fore.YELLOW+"    [8] ")
    print (Fore.YELLOW+"    [9] ")
    print (Fore.YELLOW+"    [10] ")
    print (Fore.CYAN+"\n                                     ╔═════════════╗")
    print (Fore.CYAN+'    [77] поддержка автора            ║'+Fore.YELLOW+' утилиты'+Fore.CYAN+'[91] ║')
    print (Fore.CYAN+'    [66] тг канал автора             ║'+Fore.YELLOW+' забавы ' +Fore.CYAN+'[92] ║')
    print (Fore.CYAN+'    [99] обновить[BETA]              ║'+Fore.GREEN +'>файлы<'  +Fore.CYAN+' [93] ║')
    print (Fore.CYAN+'    [00] выход                       ╚═════════════╝')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '91':
        os.system('clear')
        os.system('python3 installer.py')
        

    if inp == '92':
        os.system('clear')
        os.system('python3 zabava.py')
        

    if inp == '93':
        os.system('clear')



    if inp == '77':
        os.system('xdg-open https://www.donationalerts.com/r/legends_never_die')


    if inp == '99':    
        os.system('git clone https://github.com/777-FOXik-777/installer')
        os.system('clear')
        print ("Загрузка...")
        time.sleep(3)
        os.chdir('installer')
        os.system('python3 fail.py')

        
    if inp == '66':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')
    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
