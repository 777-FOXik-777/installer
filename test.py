import os
import signal
import subprocess
import re
import time

def signal_handler(signal, frame):
    print('Вы нажали Ctrl+C!')
    if process:
        process.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

process = None

def get_url():
    global process
    command = "ssh -R 80:localhost:8080 nokey@localhost.run"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    output = process.stdout.readline().decode('utf-8')
    
    if output:
        os.system('clear')
        url = re.search("(https://[-0-9a-z.]*.lhr.life)", output)
        if url is not None:
            return url.group(1)

url = get_url()
if url is not None:
    print(f'URL: {url}')
else:
    print("URL не найден")
