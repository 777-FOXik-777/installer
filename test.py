import os
import time
from colorama import Fore
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT



def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)


def setup():
    time.sleep(2)
    bgtask("ssh -R 80:localhost:8080 nokey@localhost.run")
    cf_success = False
    for i in range(10):
        cf_url = re.search("(https://[-0-9a-z.]*.lhr.life)")
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
    print(f'\n[~] Link: {cf_url}')


setup()
