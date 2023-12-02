#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    Funtion to print a response of a specific url
    """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf8')))

if __name__ == "__main__":
    main()
