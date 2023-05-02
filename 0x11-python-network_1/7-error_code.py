#!/usr/bin/python3
"""It take a script on a URL and send it to URL and display to it response"""

import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
