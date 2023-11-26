import subprocess
import time

cmd = "ssh -R 80:localhost:8080 nokey@localhost.run"
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

cf_success = False
cf_url = ""
for i in range(10):
    line = p.stdout.readline().decode('utf-8')
    if "https://[-0-9a-z.]*.lhr.life)" in line:
        cf_url = line.strip()
        cf_success = True
        break
    time.sleep(1)

print(f'\n[~] Link: {cf_url}')
