#!/usr/bin/python3
""" function """


def append_write(filename="", text=""):
    """ read file """

    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
