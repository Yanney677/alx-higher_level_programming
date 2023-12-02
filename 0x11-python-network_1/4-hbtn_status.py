#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    
    sew = requests.get("https://intranet.hbtn.io/status")
    print("Body response")
    print("\t- type: {}".format(type(sew.text)))
    print("\t- content: {}".format(sew.text))
