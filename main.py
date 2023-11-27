import subprocess
import re
import select
import time

def get_url(timeout=10):
    # Запускаем команду SSH в фоновом режиме
    try:
        p = subprocess.Popen("ssh -R 80:8080 nokey@localhost.run -T -n", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Ошибка при запуске команды SSH: {e}")
        return ""

    # Читаем вывод команды SSH и ищем URL
    start_time = time.time()
    while True:
        # Проверяем, не истекло ли время ожидания
        if time.time() - start_time > timeout:
            print("Время ожидания истекло")
            return ""

        # Читаем из stdout, если есть что читать
        if select.select([p.stdout], [], [], 0.0)[0]:
            output = p.stdout.read().decode('utf-8')
            match = re.search("(https://[-0-9a-z.]*.lhr.life)", output)

            # Возвращаем URL или продолжаем ожидание, если URL не найден
            if match:
                return match.group(0)

    return ""

print(f'\n[~] Ссылка: {get_url()}')
