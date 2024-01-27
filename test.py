import requests
import subprocess

url = "https://www.olx.ua/uk/"

response = requests.get(url)

if response.status_code == 200:
    with open("page.html", "wb") as f:
        f.write(response.content)

    ssh_command = "ssh -R 80:localhost:8080 nokey@localhost.run -T -n 2>&1 | awk '/.lhr.life/ {print $6}'"
    url = subprocess.getoutput(ssh_command)

    print(url)
