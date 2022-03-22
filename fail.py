import os, time, webbrowser
    
os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <файлы>]')
    time.sleep(3)
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
    print (Fore.YELLOW+"    [1] тунелирование <ngrok>")
    print (Fore.YELLOW+"    [2] тунелирование <localhost>")
    print (Fore.YELLOW+"    [3] фишинг <PyPhisher>")
    print (Fore.YELLOW+"    [4] ддос <Doser>")
    print (Fore.YELLOW+"    [5] заблокировать Termux <!!ОПАСНО!!>")
    print (Fore.YELLOW+"    [6] просмотр взломаных камер <CAM-HACKERS>")
    print (Fore.YELLOW+"    [7] получить вирус ссылку <android>")
    print (Fore.YELLOW+"    [8] замаскировать фишинг <maskphish>")
    print (Fore.YELLOW+"    [9] пробив по номеру <phoneinfoga>")
    print (Fore.YELLOW+"    [10] пробив по ip <Uti-lite>")
    print (Fore.CYAN+"\n                                     ╔═════════════╗")
    print (Fore.CYAN+'    [77] поддержка автора            ║'+Fore.YELLOW+' утилиты'+Fore.CYAN+'[91]║ ')
    print (Fore.CYAN+'    [66] тг канал автора             ║'+Fore.YELLOW+' забавы ' +Fore.CYAN+'[92] ║')
    print (Fore.CYAN+'    [99] обновить[BETA]              ║'+Fore.GREEN +'>файлы<'  +Fore.CYAN+' [93] ║')
    print (Fore.CYAN+'    [00] выход                       ╚═════════════╝')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '91':
        os.system('clear')
        print(Fore.RED+'[меню <утилиты>]')
        time.sleep(3)
        os.system('python3 install.py')
        res()

    if inp == '92':
        os.system('clear')
        print(Fore.RED+'[меню <забавы>]')
        time.sleep(3)
        os.system('python3 zabava.py')
        res()

     if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
        
