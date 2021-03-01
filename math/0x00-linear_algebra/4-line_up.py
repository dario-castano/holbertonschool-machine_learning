#!/usr/bin/env python3
"""Task 4. Line Up"""


def add_arrays(arr1, arr2):
    """Adds two lists"""
    return list(map(lambda x, y: x+y, arr1, arr2)) if len(arr1) == len(arr2) else None
