#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from sanic import Sanic 
from sanic.response import text

app = Sanic()

@app.route("/")
async def index(request):
    return text('')


@app.route("/user/<id:int>", methods=['GET'])
async def user_info(request, id):
    return text(str(id))


@app.route("/user", methods=['POST'])
async def user(request):
    return  text('')


if __name__ == '__main__':
    app.run(port=3000, log_config=None, debug=False)