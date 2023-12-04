# Импортируем модули re и subprocess для работы с регулярными выражениями и запуска команды ssh
import re
import subprocess

# Определяем имя файла, в который записывается вывод команды ssh
cf_file = "logs/lh.log"

# Определяем функцию для поиска строки, соответствующей регулярному выражению, в файле
def grep(pattern, file):
    with open(file, "r") as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                return match.group(1)
    return ""

# Определяем функцию для запуска команды в фоновом режиме и перенаправления ее вывода в файл
def bgtask(command, stdout, stderr, cwd="./"):
    try:
        return subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        # Если возникла ошибка, записываем ее в файл error.log
        with open("error.log", "a") as file:
            file.write(str(e) + "\n")

# Открываем файл для записи вывода команды ssh
cf_log = open(cf_file, "w")

# Запускаем команду ssh в фоновом режиме и перенаправляем ее вывод в файл
bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=cf_log, stderr=cf_log)

# Пытаемся найти URL в файле в течение 10 секунд
cf_success = False
for i in range(10):
    cf_url = grep("(https://[-0-9a-z.]*.lhr.life)", cf_file)
    if cf_url != "":
        cf_success = True
        break
    time.sleep(1)

# Выводим найденный URL на экран
print(f'\n[~] Link: {cf_url}')

# Закрываем файл
cf_log.close()

