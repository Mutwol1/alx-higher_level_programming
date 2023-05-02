#!/usr/bin/python3
"""It take a URL and it send it to a display of a X-Request-Id"""

import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('x-Request-Id'))
