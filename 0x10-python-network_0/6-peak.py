#!/usr/bin/python3
""" a python function to identify the peak of the list"""

def find_peak(list_of_integers):
    """a function to return the maximum number of a list"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
