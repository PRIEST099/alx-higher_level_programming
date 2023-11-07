#!/usr/bin/python3
"""a module to use JSON"""


def to_json_string(my_obj):
    import json
    representation = json.dumps(my_obj)
    return representation
