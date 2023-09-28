#!/usr/bin/python3
""" Function find_peak that finds a peak in a list of integers."""


def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers"""
    pre = 0
    for index, val in enumerate(list_of_integers):
        if index:
            pre = list_of_integers[index - 1]
        if index < len(list_of_integers) - 1:
            next = list_of_integers[index + 1]
        else:
            next = 0
        if val >= pre and val >= next:
            return val
