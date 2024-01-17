import os, time, sys

from colorama import Fore, Style


def baner():
    os.system('clear')
    os.system('lolcat ~/installer/banner/baner.txt')










baner()
print(Fore.WHITE+'', Style.BRIGHT)
print (Fore.YELLOW+" ["+Fore.CYAN+"~"+Fore.YELLOW+"] Проверка наличий обновления...")
print(Fore.WHITE+'', Style.BRIGHT)
time.sleep(1)


os.chdir('/data/data/com.termux/files/home/installer/Installer_Files/trash')


os.system('git clone --depth 1  https://github.com/777-FOXik-777/installer updatepak')

def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        return file1.read() == file2.read()



# Пример использования
file1_path = "/data/data/com.termux/files/home/installer/Installer_Files/trash/updatepak/Installer_Files/about/version"
file2_path = "/data/data/com.termux/files/home/installer/Installer_Files/about/version"

result = compare_files(file1_path, file2_path)

if result:
    os.system('rm -fr /data/data/com.termux/files/home/installer/Installer_Files/trash/updatepak')
    baner()
    print(Fore.WHITE+'', Style.BRIGHT)
    print (Fore.YELLOW+" ["+Fore.RED+"~"+Fore.YELLOW+"] Обновлений нет!")
    print(Fore.WHITE+'', Style.BRIGHT)
    tsu = input(' [Нажмите Enter чтобы продолжить]')
    os.system('clear')

else:
    os.system('rm -fr /data/data/com.termux/files/home/installer/Installer_Files/trash/updatepak')
    baner()
    print(Fore.WHITE+'', Style.BRIGHT)
    print (Fore.GREEN+" ["+Fore.CYAN+"!"+Fore.GREEN+"] Есть обновление!")
    print(Fore.WHITE+'', Style.BRIGHT)
    print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Обновить Installer ?")
    print(Style.RESET_ALL)
    uodate = input(' Выбери пункт [y/n] ➤ ')
    
    if uodate == 'y':
        os.system('rm -fr /data/data/com.termux/files/home/setup_installer.py')
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('mv setup_installer.py /data/data/com.termux/files/home/')
        os.system("""sed -i '/^cd && cd installer && python testinstaller.py$/d' ~/.bashrc""")
        os.system('echo "cd && python setup_installer.py" >> ~/.bashrc')
        print(f'\33]0; Создайте новый сезон!\a',
                end='', flush=True)  
        while True:
            os.system('clear')
            baner()
            print(Fore.WHITE+'', Style.BRIGHT)
            print(Style.BRIGHT, Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Перезапустите Termux или создайте новый сезон!")
            lol = input('')
            
    else:
        os.system('clear')









