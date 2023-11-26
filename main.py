import os
import time
import re
import subprocess

# Запускаем команду SSH в фоновом режиме
p = subprocess.Popen(["ssh", "-R", "80:localhost:8080", "localhost.run", "-T", "-n"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

cf_success = False
cf_url = ""
for i in range(10):
    # Читаем вывод команды SSH
    output = p.stdout.read().decode('utf-8')
    # Ищем URL в выводе
    match = re.search("(https://[-0-9a-z.]*.lhr.life)", output)
    if match:
        cf_url = match.group(0)
        cf_success = True
        break
    time.sleep(1)

print(f'\n[~] Link: {cf_url}')
