#!/bin/bash
#To display HTTP to a given server and given URL an accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
