import os
import time
import re
import subprocess

def bgtask(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd="./"):
    try:
        return subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        print(e)

# Запускаем команду SSH в фоновом режиме
p = bgtask("ssh -R 80:localhost:8080 localhost.run")
cf_url = ""
for i in range(10):
    # Читаем вывод команды SSH
    output = p.stdout.read().decode('utf-8')
    # Ищем URL в выводе
    match = re.search("(.lhr.life)", output)
    if match:
        cf_url = match.group(0)
        cf_success = True
        break
    time.sleep(1)

print(f'\n[~] Link: {cf_url}')
