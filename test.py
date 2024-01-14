import os, time

from colorama import Fore, Style

os.system('clear')


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


def compare_files(file_path1, file_path2):
    os.chdir('/data/data/com.termux/files/home/Installer_Files/version')
  
    os.system('wget -O chek https://raw.githubusercontent.com/777-FOXik-777/installer/main/Installer_Files/version')
  
    try:
        # Открываем первый файл для чтения
        with open(file_path1, 'r') as file1:
            content1 = file1.read()

        # Открываем второй файл для чтения
        with open(file_path2, 'r') as file2:
            content2 = file2.read()

        # Сравниваем содержимое файлов
        if content1 == content2:
            print(f"Нет обновлений!")
        else:
            print(f"Есть обновление!")
    except FileNotFoundError:
        print("Один из файлов не найден.")
    except Exception as e:
        print(f"Произошла ошибка при сравнении файлов: {e}")

# Пример использования
compare_files("/data/data/com.termux/files/home/Installer_Files/version/chek", "/data/data/com.termux/files/home/Installer_Files/version/3.0.0")
