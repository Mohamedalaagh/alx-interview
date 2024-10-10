#!/usr/bin/python3
"""
module that checks if all boxes can be unlocjed
"""


def canUnlockAll(boxes):
    """Function checks if all boxes can be unlocked

    Args:
        boxes (list of list of int): a list where each index represent a box
                                    and each box might contains a keys that
                                    can unlock other boxes

    Returns:
        bool: True if all boxes can be unlocked, False if failed
    """
    stack = [i for i in range(0, len(boxes))]
    keys = [0]
    loop = 0

    while loop == 0:
        if not stack:
            break

        for i in stack:
            if i in keys:
                temp = stack.pop(stack.index(i))
                break

        for i in boxes[temp]:
            if i not in keys:
                keys.append(i)

        if all(elem not in keys for elem in stack):
            loop = 1

    if len(stack) == 0:
        return True
    else:
        return False
