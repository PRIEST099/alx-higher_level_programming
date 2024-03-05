#!/bin/bash
# a script to send a post method wit json data
curl -s -X POST -H "Content-Type: application/json" --data-raw "@$2" "$1"
