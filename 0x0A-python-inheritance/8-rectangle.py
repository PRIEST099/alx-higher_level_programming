#!/usr/bin/python3
"""defines a class rectangel"""
BaseGeometry = __import__('7-base_goeometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
