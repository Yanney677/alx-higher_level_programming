#!/usr/bin/python3
"""
    Script that takes in a letter and sends a POST request to
    https://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    eq = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        eq_json = eq.json()
        if eq_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(eq_json['id'], eq_json['name']))
    except ValueError:
        print("Not a valid JSON")
