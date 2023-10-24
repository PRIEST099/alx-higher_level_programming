#!/usr/bin/python3
"""Module interpreter"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """constructor object.
        Args:
        size(int): length of the side of the square
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raies ValueError("size must be >= 0")
