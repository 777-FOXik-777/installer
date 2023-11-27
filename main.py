import subprocess
import re

# Запускаем команду SSH в фоновом режиме
p = subprocess.Popen(["ssh", "-R", "80:8080", "nokey@localhost.run", "-T", "-n"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

cf_url = ""
for i in range(10):
    # Читаем вывод команды SSH
    output = p.stdout.read().decode('utf-8')
    # Ищем URL в выводе
    match = re.search("(https://[-0-9a-z.]*.lhr.life)", output)
    if match:
        cf_url = match.group(0)
        break

print(f'\n[~] Link: {cf_url}')
