#!/bin/bash
#It is a request that is given to a URL anddisply the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
