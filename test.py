import subprocess
import re
import os

def get_url():
    command = "ssh -R 80:localhost:8080 nokey@localhost.run"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    while True:
        os.system('clear')
        output = process.stdout.readline().decode('utf-8')
        url = re.search("(https://[-0-9a-z.]*.lhr.life)", output)
        if url is not None:
            process.terminate()
            return url.group(1)

url = get_url()
print(f'URL: {url}' if url else "URL не найден")
