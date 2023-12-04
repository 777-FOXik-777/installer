# Импортируем модули subprocess и re для запуска команды ssh и работы с регулярными выражениями
import subprocess
import re

# Задаем регулярное выражение для поиска ссылки
regex = "(https://[-0-9a-z.]*.lhr.life)"

# Запускаем команду ssh с нужными параметрами и получаем вывод в переменную output
output = subprocess.run(["ssh", "-R", "80:localhost:8080", "nokey@localhost.run", "-T", "-n"], capture_output=True, text=True).stdout

# Используем функцию re.search для поиска первого совпадения регулярного выражения в выводе
match = re.search(regex, output)

# Проверяем, что совпадение найдено
if match:
    # Выводим найденную ссылку на экран
    print(match.group(0))
else:
    # Выводим сообщение, что ссылка не найдена
    print("Ссылка не найдена")
