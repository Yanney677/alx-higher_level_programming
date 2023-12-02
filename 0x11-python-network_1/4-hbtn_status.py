#!/usr/bin/python3
"""script that fetches model
"""
import requests

if __name__ == "__main__":
    sew = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response")
    print("\t- type: {}".format(sew.text.__class__))
    print("\t- content: {}".format(sew.text))
