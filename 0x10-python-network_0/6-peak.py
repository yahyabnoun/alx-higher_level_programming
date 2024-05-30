#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def find_peak_util(arr, low, high, n):
        mid = low + (high - low) // 2
        
        # Check if mid element is greater than its neighbors
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]
        # If the left neighbor is greater, then the peak lies on the left side
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1, n)
        # If the right neighbor is greater, then the peak lies on the right side
        else:
            return find_peak_util(arr, mid + 1, high, n)

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1, len(list_of_integers))
