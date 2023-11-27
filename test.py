import os
from re import search
from subprocess import Popen, PIPE, DEVNULL

def cat(file):
    if os.path.isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

def grep(regex, target):
    content = cat(target) if os.path.isfile(target) else target
    results = search(regex, content)
    return results.group(1) if results is not None else ""

def bgtask(command, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=PIPE, stderr=DEVNULL, cwd=cwd)
    except Exception as e:
        with open("logs/error.log", "a") as error_file:
            error_file.write(str(e))

def setup():
    bgtask("ssh -R 80:localhost:8080 nokey@localhost.run")
    for _ in range(10):
        cf_url = grep("(https://[-0-9a-z.]*.lhr.life)", "logs/lh.log")
    print(f'\n[~] Link: {cf_url}')


setup()
