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

def compare_filenames_in_folder(folder_path, filename_to_compare):
    
    os.chdir('/data/data/com.termux/files/home/Installer_Files/version')
  
    os.system('wget -O chek https://raw.githubusercontent.com/777-FOXik-777/installer/main/Installer_Files/version')
  
    
    # Получаем список файлов в указанной папке
    files_in_folder = os.listdir(folder_path)

    # Проверяем наличие файла с нужным именем в папке
    if filename_to_compare in files_in_folder:
        print(f"Обновления нету!")
    else:
        print(f"Есть обновление!")

# Пример использования
folder_path = "/data/data/com.termux/files/home/Installer_Files/version/chek/"
filename_to_compare = "3.0.0"

compare_filenames_in_folder(folder_path, filename_to_compare)
