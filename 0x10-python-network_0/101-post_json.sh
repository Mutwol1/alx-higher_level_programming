#!/bin/bash
#To send JSON POST WITH GIVEN URL with a JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
