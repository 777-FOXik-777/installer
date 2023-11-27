import subprocess
import re

def setup(site):
    time.sleep(2)
    bgtask("ssh -R 80:localhost:8080 nokey@localhost.run", stdout=cf_log, stderr=cf_log)
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]*.lhr.life)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
    print(f'\n[~] Link: {cf_url}')


setup(site)
