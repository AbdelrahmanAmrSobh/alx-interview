#!/usr/bin/python3
"""Module with canUnlockAll method that check if we can unlock each box in list of boxes.

First box in list is always unlocked and can hold keys for boxes.
"""


def addKeys(keys, newKeys, size):
    """
    Method that handle adding new keys to keys

    Conditions:
    -----------
        Each key has to be unique
        Each key has to be in range(1, size)

    If key already exist or not in range key is skipped.
    """
    for newKey in newKeys:
        if size > newKey > 0 and newKey not in keys:
            keys.append(newKey)


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Parameter:
    ----------
    boxes: list[list]:
        boxes is list of list (list of boxes each box is a list)
    Returns True or False.
    """
    size = len(boxes)
    if size < 2:
        return True
    keys = []
    addKeys(keys, boxes[0], size)
    index = 0
    while True:
        length = len(keys)
        if index == length:
            break
        key = keys[index]
        newKeys = boxes[key]
        addKeys(keys, newKeys, size)
        index += 1
    return len(keys) == size - 1
