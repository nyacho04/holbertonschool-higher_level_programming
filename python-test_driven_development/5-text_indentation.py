#!/usr/bin/python3
"""
this module contains a function that prints a text with 2 new lines
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    args:text (str): the text to be formatted
    raises:TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    charc = ['.', '?', ':']
    result = ""
    a = 0
    while a < len(text):
        result += text[a]
        if text[a] in charc:
            result += "\n\n"
            a += 1
            while a < len(text) and text[a] == ' ':
                a += 1
            continue
        a += 1
    print(result, end="")
