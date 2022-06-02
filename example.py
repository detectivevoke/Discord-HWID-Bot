import requests
import socket
import subprocess
import json

config = json.loads(open("config.json","r").read())
def check_auth():
    

    hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())

    req = requests.post(config["url"]+"/database", data={"hwid": hwid})
    print(req.content)
    if "wasd" in str(req.content):
        return True
    else:
        return False

check_auth()