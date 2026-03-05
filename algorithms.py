from dataclasses import dataclass


@dataclass
class AlgorithmReport:
    sortedArray: list[int]
    numberOfComparisions: int


def generateArrayOfAllPossiblePermutations(n: int) -> list[list[int]]:
    """
    Generates all possible permutations of integers from 0 to n-1.

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        n (int): The size of the integer array to permute.

    Returns:
        list[list[int]]: A list containing all permutations
    """
    pass


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
    pass


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
    pass


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
    pass


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
    pass
