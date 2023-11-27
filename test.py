import os
import time
from colorama import Fore
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT

global site

def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

cf_file = "logs/lh.log"
cf_log = open(cf_file, 'w')

def setup():
    bgtask("ssh -R 80:localhost:8080 localhost.run -T -n", stdout=cf_log, stderr=cf_log)
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]*.lhr.life)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
    print(f'\n[~] Link: {cf_url}')


setup()
