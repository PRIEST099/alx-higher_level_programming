#!/bin/bash
#a script to send a request and retrieves only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
