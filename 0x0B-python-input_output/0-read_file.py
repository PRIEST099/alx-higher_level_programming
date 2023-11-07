#!/usr/bin/python3
"""a module for reading from a file"""


def read_file(filename=""):
    """a function that reads a text file and prints it out"""

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
