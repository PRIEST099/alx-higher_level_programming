#!/bin/bash
#a script to use a post request with some header params
curl -s -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
