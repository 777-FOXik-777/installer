import subprocess
import re

def get_url():
    command = "ssh -R 80:localhost:8080 nokey@localhost.run"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error is not None:
        print(f"Произошла ошибка: {error}")
        return None

    url = re.search("(https://[-0-9a-z.]*.lhr.life)", output.decode('utf-8'))
    if url is not None:
        return url.group(1)

    return None

url = get_url()
if url is not None:
    print(f'URL: {url}')
else:
    print("URL не найден")
