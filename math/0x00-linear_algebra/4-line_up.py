#!/usr/bin/env python3
"""Task 4. Line Up"""


def add_arrays(arr1, arr2):
    """Adds two lists"""
    return list(map(lambda x, y: x+y, arr1, arr2)) if eq(arr1, arr2) else None


def eq(arr1, arr2):
    """Checks if 2 lists are Equal"""
    return len(arr1) == len(arr2)
