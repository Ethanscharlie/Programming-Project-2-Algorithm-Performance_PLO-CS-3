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

        output.append(array.copy())
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

    def merge(report: AlgorithmReport, left: int, middle: int, right: int) -> None:
        leftAuxiliaryArray = [0] * (middle - left + 1)
        rightAuxiliaryArray = [0] * (right - middle)

        for i in range(len(leftAuxiliaryArray)):
            leftAuxiliaryArray[i] = report.sortedArray[left + i]

        for i in range(len(rightAuxiliaryArray)):
            rightAuxiliaryArray[i] = report.sortedArray[middle + 1 + i]

        leftIndex = 0
        rightIndex = 0
        k = left
        while leftIndex < len(leftAuxiliaryArray) and rightIndex < len(rightAuxiliaryArray):
            if leftAuxiliaryArray[leftIndex] <= rightAuxiliaryArray[rightIndex]:
                report.sortedArray[k] = leftAuxiliaryArray[leftIndex]
                leftIndex += 1
            else:
                report.sortedArray[k] = rightAuxiliaryArray[rightIndex]
                rightIndex += 1

            k += 1
            report.numberOfComparisions += 1

        while leftIndex < len(leftAuxiliaryArray):
            report.sortedArray[k] = leftAuxiliaryArray[leftIndex]
            leftIndex += 1
            k += 1

        while rightIndex < len(rightAuxiliaryArray):
            report.sortedArray[k] = rightAuxiliaryArray[rightIndex]
            rightIndex += 1
            k += 1

    def mergesort(report: AlgorithmReport, left: int, right: int) -> None:
        if left >= right:
            return

        middle = (left + right) // 2
        mergesort(report, left, middle)
        mergesort(report, middle + 1, right)
        merge(report, left, middle, right)

    report = AlgorithmReport(array.copy(), 0)
    mergesort(report, 0, len(report.sortedArray) - 1)
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
    Sorts an array of integers using the Shaker Sort algorithm. 
    Also known as Bidirectional Bubble Sort and Cocktail Sort.

    Sources: 
        https://www.geeksforgeeks.org/dsa/cocktail-sort/
        https://en.wikipedia.org/wiki/Cocktail_shaker_sort

    Expected results:
        Best Case O(n)
        Average Case O(n^2)
        Worst Case O(n^2)
        Space O(1) Auxiliary Space
        Maximum Number of Comparisons O(n^2)

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        array (list[int]): The unsorted array of integers to be sorted.

    Returns:
        AlgorithmReport: containing a sorted array and the number of comparisions used.
    
    Author: TheodoreT
    """
    # Keeps track of any swaps that occur to know when to stop the while loop.
    # True means at least one swap was performed, 
    # False means no swaps were performed.
    swapPerformed = True 
    # Gets and stores the beginning and end indices of the array.
    # These are used to know when to stop "going through the array".
    arrayLength = len(array) # "array" is the name of the local variable.
    startIndex = 0
    endIndex = arrayLength - 1

    # Loop Stages 1 & 2 until no swaps are performed in either Stage 1 or Stage 2.
    while (swapPerformed == True):
        # Resets swapPerformed to False in case it was True in a previous iteration.
        swapPerformed = False

        # <-- Stage 1: Loop through array from left to right. -->
        for i in range(startIndex, endIndex):
            # Checks if current element is bigger than next element.
            if (array[i] > a[i + 1]):
                # Swaps bigger current element with the smaller next element.
                array[i], array[i + 1] = array[i + 1], array[i]
                swapPerformed = True # Marks that a swap has been performed.
            report.numberOfComparisons += 1 # Counts comparison.
        # If a swap was not performed, that means array is sorted and while loop can end.
        if (swapPerformed == False): break
        # Largest number is now at the end of the array after loop, 
        # so we no longer need to sort that element from now on.
        endIndex = endIndex - 1

        # Resets swapPerformed to False in case it was True in the previous stage.
        swapPerformed = False

        # <-- Stage 2: Loop through array backwards from right to left. -->
        # Both startIndex and endIndex need to be subtracted by 1 so that 
        # the pair of elements being compared can be i and i+1, 
        # since i-1 at i=0 does not work (out of bounds).
        for i in range(endIndex - 1, startIndex - 1, -1):
            # Checks if current element is bigger than next element.
            if (array[i] > a[i + 1]):
                # Swaps bigger current element with the smaller next element.
                array[i], array[i + 1] = array[i + 1], array[i]
                swapPerformed = True # Marks that a swap has been performed.
            report.numberOfComparisons += 1 # Counts comparison.
        # If a swap was not performed, that means array is sorted and while loop can end.
        if (swapPerformed == False): break
        # Smallest number is now at the beginning of the array after loop, 
        # so we no longer need to sort that element from now on.
        startIndex = startIndex + 1

    # Creates the report to be returned based on the sorted array.
    report = AlgorithmReport(array.copy(), 0) # numberOfComparisons is already counted.
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
