import requests
import subprocess
import tempfile
import os

# Замените 'ваша_ссылка' на фактическую ссылку страницы
url = 'ваша_ссылка'

# Скачиваем страницу
response = requests.get(url)
html_content = response.text

# Создаем временный файл для сохранения скачанной страницы
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
    temp_file.write(html_content)
    temp_file_path = temp_file.name

# Команда для отправки файла на удаленный сервер через ssh
ssh_command = f'ssh -R 80:localhost:8080 nokey@localhost.run -T -n "cat > ~/remote_page.html" < {temp_file_path}'

# Выполняем команду через subprocess
subprocess.run(ssh_command, shell=True)

# Удаляем временный файл
os.remove(temp_file_path)

# Получаем URL удаленной страницы
remote_page_url_command = 'ssh -R 80:localhost:8080 nokey@localhost.run -T -n 2>&1 | awk \'/.lhr.life/ {print $6}\''
remote_page_url = subprocess.getoutput(remote_page_url_command)

print(f'Страница доступна по URL: {remote_page_url}')
