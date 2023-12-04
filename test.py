# Импортируем модуль subprocess для запуска команды ssh
import subprocess

# Запускаем команду ssh с нужными параметрами и получаем вывод в переменную output
output = subprocess.run(["ssh", "-R", "80:localhost:8080", "nokey@localhost.run", "-T", "-n"], capture_output=True, text=True).stdout

# Ищем в выводе ссылку, которая заканчивается на .lhr.life, и выводим ее на экран
for line in output.splitlines():
    if line.endswith(".lhr.life"):
        print(line)
        break


