#!/usr/bin/python3
"""
    Script that takes GitHub Credentials (username and password)
    used GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    eq = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    eq_json = eq.json()
    if eq_json == {}:
        print("None")
    else:
        print("{}".format(eq_json.get('id')))
