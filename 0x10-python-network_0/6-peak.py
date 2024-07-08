#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Find a peak element in an list_of_integersay.

    A peak element is an element that is greater than its neighbors.

    Args:
        list_of_integers (list): The input array.

    Returns:
        int: The peak element in the list_of_integersay.
        If the array is empty, None is returned.

    """
    # Base case: if the list_of_integersay is empty, return None
    if not list_of_integers:
        return None

    # Initialize left and right pointers
    left, right = 0, len(list_of_integers) - 1

    # Perform binary search to find the peak element
    while left < right:
        mid = (left + right) // 2

        # If the middle element is less than its right neighbor,
        # then the peak element must be to the right of the middle
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # Return the left pointer, which points to the peak element
    return list_of_integers[left]
