#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): List of boxes, each containing keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    #
    n = len(boxes)
    opened = set([0])  # start with box 0 unlocked
    stack = [0]  # keys to explore, starting with box 0

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened and key < n:
                opened.add(key)
                stack.append(key)

    # Check if all boxes are opened
    return len(opened) == n
