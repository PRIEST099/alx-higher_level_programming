#!/usr/bin/python3
"""a module that represents a student class dictionsary"""


class Student:
    """represents a student"""

    def __init___(self, first_name, last_name, age):
        """a function to initalise class variables"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of an object"""
        return self.__dict__
