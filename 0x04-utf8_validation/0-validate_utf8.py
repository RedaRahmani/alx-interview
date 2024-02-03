#!/usr/bin/python3
"""This script contains a method that determines
if a given data set represents a valid UTF-8 encoding.

Each integer represents 1 byte of data,
therefore you only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """ return: True if data is valid UTF-8 encoding, else returns False """

    result = [i & 255 for i in data]
    try:
        bytes(result).decode()
    except UnicodeError:
        return False
    else:
        return True