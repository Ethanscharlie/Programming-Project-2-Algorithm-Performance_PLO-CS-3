"""
Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran
CS 2430 Team 6
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026
Primary author: Ethan J. Hadley
"""

from dataclasses import dataclass


@dataclass
class AlgorithmReport:
    sortedArray: list[int]
    numberOfComparisions: int


def generateArrayOfAllPossiblePermutations(n: int) -> list[list[int]]:
    """
    Generates all possible permutations of integers from 0 to n-1.

    For example, if n = 3, your generator must produce:
    {0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}

    This implementation is based on the non-recursive format of heaps algorithm (https://en.wikipedia.org/wiki/Heap's_algorithm)

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        n (int): The size of the integer array to permute.

    Returns:
        list[list[int]]: A list containing all permutations
    """

    output = []

    # For example n = 3 will look like [ 0, 1, 2 ]
    array = [i for i in range(n)]

    auxiliaryArray = [0] * n
    output.append(array)

    i = 1
    while i < n:
        if auxiliaryArray[i] >= i:
            auxiliaryArray[i] = 0
            i += 1
            continue

        indexIsEven = i % 2 == 0
        if indexIsEven:
            # Simple way of swapping in python using tuple unpacking
            array[0], array[i] = array[i], array[0]
        else:
            array[auxiliaryArray[i]], array[i] = array[i], array[auxiliaryArray[i]]

        output.append(array)
        auxiliaryArray[i] += 1
        i = 1

    return output


def mergesort(array: list[int]) -> AlgorithmReport:
    """
    Sorts an array of integers using the mergesort algorithm.

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        array (list[int]): The unsorted array of integers to be sorted.

    Returns:
        AlgorithmReport: containing a sorted array and the number of comparisions used.
    """

    report = AlgorithmReport()
    return report


def quicksort(array: list[int]) -> AlgorithmReport:
    """
    Sorts an array of integers using the quicksort algorithm.

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        array (list[int]): The unsorted array of integers to be sorted.

    Returns:
        AlgorithmReport: containing a sorted array and the number of comparisions used.
    """

    report = AlgorithmReport()
    return report


def shakerSort(array: list[int]) -> AlgorithmReport:
    """
    Sorts an array of integers using shaker sort (aka bidirectional bubble sort).

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        array (list[int]): The unsorted array of integers to be sorted.

    Returns:
        AlgorithmReport: containing a sorted array and the number of comparisions used.
    """

    report = AlgorithmReport()
    return report


def heapsort(array: list[int]) -> AlgorithmReport:
    """
    Sorts an array of integers using the heapsort algorithm.

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        array (list[int]): The unsorted array of integers to be sorted.

    Returns:
        AlgorithmReport: containing a sorted array and the number of comparisions used.
    """

    report = AlgorithmReport()
    return report
