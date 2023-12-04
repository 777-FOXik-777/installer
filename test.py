# Импортируем модуль subprocess для запуска команды ssh
import subprocess

# Запускаем команду ssh с нужными параметрами и получаем ее вывод
output = subprocess.run(["ssh", "-R", "80:localhost:8080", "nokey@localhost.run", "-T", "-n"], capture_output=True, text=True)

# Ищем в выводе строку, начинающуюся с https://
for line in output.stdout.splitlines():
    if line.startswith("https://"):
        # Выводим найденную строку на экран
        print(line)
        # Прерываем цикл
        break
