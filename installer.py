import os, time

filename = "tg_SYPEXHACK"

if os.path.exists(filename):

    print ('[~] Установка зависимостей... \n')
    time.sleep(2)
    os.system('clear')
       
    #colorama
    print ('[~] Установка colorama... \n')
    time.sleep(1.5)
    os.system('pip install colorama')
    os.system('clear')
    
    from colorama import Fore, Style

    print ('\n')
    def res():
        print(Style.RESET_ALL)
      
    #питон
    
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python2...")
    res()
    time.sleep(1.5)
    os.system('pkg install python2 -y')
    os.system('clear')
    
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python3...")
    res()
    time.sleep(1.5)
    os.system('pkg install python3 -y')
    
    #доступ к файлам
    
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Разрешите доступ к файлам")
    res()
    time.sleep(1.5)
    os.system('termux-setup-storage')
    tsu = input('\n[Нажмите enter чтобы продолжить]')
    os.system('clear')


    os.system('rm -fr tg_SYPEXHACK')
    
    #запуск
    
    os.system('clear')
    os.system('xdg-open https://t.me/+p9CBKAxQUQZmMjli')
    os.system('python3 tool.py')
    

else:
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"]Все зависимости уже установлены!...")
    time.sleep(2)
    os.system('clear')
    os.system('python3 tool.py')
        
