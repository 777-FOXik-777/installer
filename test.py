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

def bgtask(command, stdout, stderr, cwd="./"):
    # Пытаемся запустить команду в фоновом режиме и вернуть объект процесса
    try:
        return subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)

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
