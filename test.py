import subprocess
import re
import time

def get_url():
    command = "ssh -R 80:localhost:8080 nokey@localhost.run"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    while True:
        output = process.stdout.readline().decode('utf-8')
        if output == '' and process.poll() is not None:
            break
        if output:
            url = re.search("(https://[-0-9a-z.]*.lhr.life)", output)
            if url is not None:
                return url.group(1)
        time.sleep(1)

    return None

url = get_url()
if url is not None:
    print(f'URL: {url}')
else:
    print("URL не найден")

