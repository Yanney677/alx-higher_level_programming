#!/usr/bin/python3
"""
    Script that takes in a URL and an email sends a POST request to that URL
    with the email as a parameter.
    Displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(req.text))
