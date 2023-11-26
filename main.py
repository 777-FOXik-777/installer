import os
import time
import re
import subprocess

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

bgtask("ssh -R 80:localhost:8080 localhost.run -T -n", stdout=cf_log, stderr=cf_log)
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]*.lhr.life)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
    print(f'\n[~] Link: {cf_url}')
