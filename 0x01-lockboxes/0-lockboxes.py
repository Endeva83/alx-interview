def canUnlockAll(boxes):
    n = len(boxes)
    opened_boxes = [False] * n
    opened_boxes[0] = True

    for i in range(n):
        if opened_boxes[i]:
            for key in boxes[i]:
                if key < n and not opened_boxes[key]:
                    opened_boxes[key] = True

    return all(opened_boxes)

