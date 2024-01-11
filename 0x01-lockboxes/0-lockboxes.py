#!/usr/bin/python3
"""
Interview preparation
n lockboxes
"""


def canUnlockAll(boxes):
    """
    a function that checks if all boxes can be opened
    """
    unlocked = set()

    for Id, box in enumerate(boxes):
        if len(box) == 0 or Id == 0:
            unlocked.add(Id)
        for key in box:
            if key < len(boxes) and key != Id:
                unlocked.add(key)
        if len(unlocked) == len(boxes):
            return True
    return False
