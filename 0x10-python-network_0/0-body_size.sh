#!/bin/bash
#It is the HTTP response header for URL.
curl -s "$1" | wc -c
