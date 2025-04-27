#!/usr/bin/env python3
# -*- coding: utf-8  -*-
#
# Reza (User:reza1615), 2011
# Huji (User:Huji), 2025
#
# Distributed under the terms of the MIT license.
#
from flask import Flask, Response
from proofread import run, update_ref_data


app = Flask(__name__)


@app.route("/check/<path:page>")
def check(page: str):
    result = run(page)

    response = Response(result, content_type="application/json;charset=utf8")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/update")
def update():
    result = update_ref_data()

    response = Response(result, content_type="application/json;charset=utf8")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
