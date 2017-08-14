#!/bin/env python
# -*- coding:utf-8 -*-
import json
import requests


def do_version(arg):
    try:
        r = requests.post('http://127.0.0.1:8888', data={"a":"b"})
        print r.text, r.request.headers
        return
    except Exception as e:
        print "{}".format(e)
        return


if __name__ == "__main__":
    do_version("asd")
