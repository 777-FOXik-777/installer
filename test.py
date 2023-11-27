import subprocess
import re

def url():
    # Запускаем команду SSH в фоновом режиме
    p = subprocess.Popen("ssh -R 80:8080 nokey@localhost.run -T -n", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    # Читаем вывод команды SSH и ищем URL
    output = p.stdout.read().decode('utf-8')
    match = re.search("(https://[-0-9a-z.]*.lhr.life)", output)

    # Возвращаем URL или пустую строку, если URL не найден
    return match.group(0) if match else ""

print(f'\n[~] Ссылка: ')
url()
