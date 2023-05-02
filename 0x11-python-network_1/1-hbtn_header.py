#!/usr/bin/python3
"""The Url is taken to a request display of a X-Request-Id"""
import urllib.request
from sys import argv

if len(argv) > 1:
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
