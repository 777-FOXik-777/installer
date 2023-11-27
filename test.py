import os
from re import search
from subprocess import Popen, PIPE, DEVNULL

def grep(regex, target):
    content = target
    results = search(regex, content)
    return results.group(1) if results is not None else None

def bgtask(command, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=PIPE, stderr=DEVNULL, cwd=cwd)
    except Exception as e:
        print(e)

bgtask("ssh -R 80:localhost:8080 nokey@localhost.run")

for i in range(10):
    cf_url = grep("(https://[-0-9a-z.]*.lhr.life)")

print ('{cf_url}')
