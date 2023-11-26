import subprocess
import time

cmd = "ssh -R 80:localhost:8080 nokey@localhost.run"
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

cf_success = False
cf_url = ""
for i in range(10):
    output = p.stdout.read().decode('utf-8')
    lines = output.split('\n')
    last_line = lines[-1]
    if ".lhr.life" in last_line:
        cf_url = last_line.strip()
        cf_success = True
        break
    time.sleep(1)

print(f'\n[~] Link: {cf_url}')
