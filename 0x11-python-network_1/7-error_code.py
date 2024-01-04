#!/usr/bin/python3
"""
    Script that takes in a URL sends a POST request to that URL
    Displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print("{}".format(req.text))
