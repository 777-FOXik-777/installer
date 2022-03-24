import os, time, webbrowser
    
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

os.system('git clone https://github.com/777-FOXik-777/updater-for-installer')

#питон2
os.system('pkg install python2')
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#доп.файл
os.system('pip install colorama')
os.system('clear')

os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')
os.system('pkg install cmatrix')

os.system('pkg install sl')
os.system('pkg install tty-clock')

os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

os.system('pkg install libcaca -y')
os.system('pkg install toilet')

os.system('rm ~/.bashrc')
os.system('echo "clear" >> ~/.bashrc')
os.system('echo "toilet -f mono9 -F metal Удач" >> ~/.bashrc')
os.system('echo [telegram @sypexhack желает вам хорошего дня] ~/.bashrc')

os.system('clear')
os.system('python3 tool.py')
