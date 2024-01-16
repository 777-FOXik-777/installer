import os

os.chdir('/data/data/com.termux/files/home/installer/Installer_Files/trash')


os.system('git clone --depth 1  https://github.com/777-FOXik-777/installer updatepak')

def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        return file1.read() == file2.read()

# Пример использования
file1_path = "/data/data/com.termux/files/home/installer/Installer_Files/trash/updatepak/Installer_Files/about/version"
file2_path = "/data/data/com.termux/files/home/installer/nstaller_Files/about/version"

result = compare_files(file1_path, file2_path)

if result:
    print("Содержимое файлов идентично.")
else:
    print("Содержимое файлов различно.")
