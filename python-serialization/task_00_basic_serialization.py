#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """serialization"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """serialization"""
    with open(filename, 'r') as file:
        return json.load(file)
