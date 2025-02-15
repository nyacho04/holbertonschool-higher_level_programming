#!/usr/bin/python3

""" function """

def write_file(filename="", text=""):
    """ read file """

    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
