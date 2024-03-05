#!/bin/bash
# a script to print the response body with 200 ok status code
curl -s -o /dev/stdout -w "%{http_code}" "$1"
