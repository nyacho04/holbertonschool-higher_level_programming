#!/usr/bin/python3
""" function """


import json


def load_from_json_file(filename):
    """ read file """

    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
