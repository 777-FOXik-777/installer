import os
import wget

# URL файла для скачивания
url = "https://raw.githubusercontent.com/777-FOXik-777/installer/main/Installer_Files/version/3.0.0"

# Путь к уже скачанному файлу
local_file_path = "/data/data/com.termux/files/home/installer/Installer_Files/version/3.0.0"

# Скачиваем файл
filename = wget.download(url)

# Проверяем, существует ли уже скачанный файл
if os.path.exists(local_file_path):

    # Сравниваем два файла
    with open(filename, "rb") as f1, open(local_file_path, "rb") as f2:
        diff = f1.read() != f2.read()

    # Если файлы отличаются, выводим сообщение
    if diff:
        print("Файлы отличаются!")

    # Если файлы одинаковые, выводим сообщение
    else:
        print("Файлы одинаковые.")

else:

    # Если файл не был скачан ранее, выводим сообщение
    print("Файл не был скачан ранее.")

# Удаляем временный файл
os.remove(filename)
