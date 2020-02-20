# -*- coding: utf-8 -*-
from flask import Flask, request, abort, redirect, url_for
import json
import random
import re

SIGN = "mvaPcfjdYuejfndk182K"

ALLURL = []

app = Flask(__name__)

@app.route("/")
def hello():
    check()
    ncount = len(ALLURL)
    if ncount == 0:
        return "hold on"

    rindex = random.randrange(0, ncount)
    return redirect(ALLURL[rindex])

@app.route("/del/")
def del_url():
    check()
    sign = request.args.get("sign")
    if sign != SIGN:
        return abort()

    url = request.args.get("url")
    if url in ALLURL:
        ALLURL.pop(url)
        return savedb()

    return "the url was not found"

@app.route("/add/")
def add_url():
    check()
    sign = request.args.get("sign")
    if sign != SIGN:
        return abort()

    url = request.args.get("url")
    if url in ALLURL:
        return "repeat the url"

    if not re.match(r'^https?:/{2}\w.+$', url):
        return "url invalid"

    ALLURL.append(url)
    return savedb()

@app.route("/showall/")
def showall():
    check()
    sign = request.args.get("sign")
    if sign != SIGN:
        return abort()
    return json.dumps(ALLURL)

def check():
    if len(ALLURL) == 0:
        loaddb()

def loaddb():
    app.logger.info("loaddb...")
    global ALLURL
    try:
        with open("db.json", "r") as f:
            jsonStr = json.load(f)
            jsonStr = json.dumps(jsonStr)
            ALLURL = json.loads(jsonStr)
            return "success"
    except Exception as e:
        s = "load db.json fail. err:{}".format(e)
        return s

def savedb():
    try:
        with open("db.json", "w") as f:
            jsonStr = json.dumps(ALLURL)
            f.write(jsonStr)
            return "success"
    except Exception as e:
        s = "save to db.json fail. err:{}".format(e)
        app.logger.error(s)
        return s


if __name__ == "__main__":
    app.run()