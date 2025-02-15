#!/usr/bin/python3
""" function """


def read_file(filename=""):
    """ read file """

    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
