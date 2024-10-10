def canUnlockAll(boxes):
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
