#!/usr/bin/python3
"""It is a scripr which take a URL and send it to a URL and display it value"""

import requests
from sys import argv


if __name__ == '__main__':
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)

