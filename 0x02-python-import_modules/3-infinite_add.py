#!/usr/bin/python3
from sys import argv
sum = 0
length = len(argv)
if length == 1:
    sum = 0
else:
    for i in range(1, length):
        sum += int(argv[i])
print("{}".format(sum))
