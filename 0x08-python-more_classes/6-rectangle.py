#!/usr/bin/python3
""" a module that defines a rectangle """


class Rectangle:
    """ a class that defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        result = []
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            [result.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                result.append("\n")
        return ("".join(result))

    def __repr__(self):
        result = "Rectangle(" + str(self.__width)
        result += ", " + str(self.__height) + ")"
        return result

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
