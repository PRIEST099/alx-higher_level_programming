#!/usr/bin/python3
def mafic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    return a * b - c
