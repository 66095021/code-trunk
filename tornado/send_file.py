#!/bin/env python
# -*- coding:utf-8 -*-
import json
import requests


def do_version(arg):
    try:
        files = {'file': open("/tmp/3.c", 'rb')}
        r = requests.post('http://127.0.0.1:8888', files=files)
        print r.text, r.request.headers
        return
    except Exception as e:
        print "{}".format(e)
        return


if __name__ == "__main__":
    do_version("asd")
