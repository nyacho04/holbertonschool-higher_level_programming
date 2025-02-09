#!/usr/bin/python3
"""module that defines a class MyList"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
