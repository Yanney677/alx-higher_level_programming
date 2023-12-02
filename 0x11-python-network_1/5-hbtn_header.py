#!/usr/bin/python3
"""Docs
"""
import sys
import requests

if __name__ == "__main__":
    sew = requests.get(sys.argv[1])
    print("{}".format(sew.headers['X-Request-Id']))
