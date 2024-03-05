#!/bin/bash
#a script to send a get request with some header variable
curl -s -H "X-School-User-Id: 98" "$1"
