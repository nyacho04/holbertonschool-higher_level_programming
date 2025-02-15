#!/usr/bin/python3
""" function """


import json


def save_to_json_file(my_obj, filename):
    """ read file """

    with open(filename, mode="w") as mfile:
        json.dump(my_obj, mfile)
