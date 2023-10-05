#!/usr/bin/python3
import calculator_1 as alx
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, alx.add(a, b)))
    print("{} - {} = {}".format(a, b, alx.sub(a, b)))
    print("{} * {} = {}".format(a, b, alx.mul(a, b)))
    print("{} / {} = {}".format(a, b, alx.div(a, b)))
