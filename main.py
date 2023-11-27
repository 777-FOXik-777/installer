import subprocess
import re

def bgtask(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL):
    try:
        return subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr)
    except Exception as e:
        print(e)

# Запускаем команду SSH в фоновом режиме
p = bgtask("ssh -R 80:8080 nokey@localhost.run -T -n")

cf_url = ""
for i in range(10):
    # Читаем вывод команды SSH
    output = p.stdout.read().decode('utf-8')
    # Ищем URL в выводе
    match = re.search("(https://[-0-9a-z.]*.lhr.life)", output)
    if match:
        cf_url = match.group(0)
        break

print(f'\n[~] Link: https://'+cf_url+'.lhr.life')
