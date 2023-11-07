#!/usr/bin/python3
"""a module to use JSON"""
import json


def to_json_string(my_obj):
    representation = json.dumps(my_obj)
    return representation
