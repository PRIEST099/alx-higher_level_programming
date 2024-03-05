#!/bin/bash
# a script to show allowed methods on a server
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | sed 's/Allow: //i'
