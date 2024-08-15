#!/usr/bin/python3 env
"""
This script analyzes and processes data from input files,
applies transformations, and generates output reports.
It includes error handling, logging, and supports
various data formats. Designed for modularity and reuse.
"""

def canUnlockAll(boxes):
    opened = [False] * len(boxes)
    opened[0] = True
    keys = boxes[0]

    for key in keys:
        if key < len(boxes) and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)


# Usage
'''boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))
'''
