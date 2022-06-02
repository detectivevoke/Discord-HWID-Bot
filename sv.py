from flask import Flask
from flask import Flask, request, render_template, redirect
import random
import string
import json
app = Flask(__name__)
from manager import Manage


config = json.loads(open("config.json","r").read())

@app.route("/")
def home():
    return "Welcome! Make sure to fill in all the details in 'main.py' and that the port you are running this on is open!"

@app.route("/database", methods=["POST","PUT"])
def db():
    management = Manage()
    if request.method == 'POST':
        hwid = request.form.get("hwid")
        print(hwid)
        try:
            info = management.get("hwid", str(hwid))[0]
            print(info[0])
            if hwid == info[0]:
                print("SAME")
                strw = "".join(random.choice(string.ascii_letters)for i in range(20))
                print(strw)
                string_return = "".join("wasd"+strw)
                print(string_return)
                return string_return
            else:
                return "False"
        except:
            return "False"

    elif request.method == "PUT":
        hwid = request.form["hwid"]
        ip = request.form["ip"]
        cname = request.form["cname"]
        management.insert(hwid, ip,cname)
        string_return = "".join("c"+random.choice(string.digits)for i in range(25)+"wasd"+random.choice(string.ascii_letters)for i in range(20)+"W")
        return string_return

def run():
    app.run(host=config["host"], port=config["port"])