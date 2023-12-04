# Импортируем модуль re для работы с регулярными выражениями
import re

# Определяем шаблон для поиска URL, начинающегося с https://
pattern = r"https://\S+"

# Запускаем команду ssh с нужными параметрами и получаем ее вывод в виде строки
output = subprocess.getoutput("ssh -R 80:localhost:8080 nokey@localhost.run")

# Ищем в выводе первое совпадение с шаблоном
match = re.search(pattern, output)

# Если совпадение найдено, выводим его на экран
if match:
    print(match.group())
