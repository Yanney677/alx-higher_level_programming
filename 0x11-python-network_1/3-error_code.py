#!/usr/bin/python3
"""Docs
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    eqr = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(eqr) as response:
            body = response.read()
            print("{}".format(body.decode('UTF-8')))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
