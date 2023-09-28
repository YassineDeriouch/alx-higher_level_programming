#!/usr/bin/python3
""" Function find_peak that finds a peak in a list of integers."""


def find_peak(list_of_integers):
    """ Call another function in recursive way """
    if (not len(list_of_integers)):
        return None
    return peak(list_of_integers, 0, len(list_of_integers) - 1)


def peak(arr, start, end):
    """ Find the peak element """
    if (start >= end):
        return arr[end]

    mid = int(start + (end - start) / 2)

    if (arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
        return arr[mid]
    elif (arr[mid] < arr[mid+1]):
        return peak(arr, mid+1, end)
    else:
        return peak(arr, start, mid-1)

