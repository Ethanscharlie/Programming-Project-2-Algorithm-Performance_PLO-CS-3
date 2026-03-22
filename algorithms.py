"""
Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran
CS 2430 Team 6
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026
Primary author: Ethan J. Hadley & Theodore T
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

    Author: Ethan J. Hadley
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

    Author: Ethan J. Hadley
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

    Author: Ethan J. Hadley
    """

    def quickSort(report: AlgorithmReport, low: int, high: int):
        if low >= high:
            return

        pivot = report.sortedArray[high]
        paritionIndex = low - 1

        for i in range(low, high):
            report.numberOfComparisions += 1

            if report.sortedArray[i] < pivot:
                paritionIndex += 1
                report.sortedArray[paritionIndex], report.sortedArray[i] = (
                    report.sortedArray[i],
                    report.sortedArray[paritionIndex],
                )

        report.sortedArray[paritionIndex + 1], report.sortedArray[high] = (
            report.sortedArray[high],
            report.sortedArray[paritionIndex + 1],
        )

        quickSort(report, low, paritionIndex)
        quickSort(report, paritionIndex + 2, high)

    report = AlgorithmReport(array.copy(), 0)
    quickSort(report, 0, len(array) - 1)
    return report


def shakerSort(array: list[int]) -> AlgorithmReport:
    """
    Sorts an array of integers using the Shaker Sort algorithm.
    Also known as Bidirectional Bubble Sort and Cocktail Sort.
    Shaker Sort loops through the array forwards and backwards (like a cocktail shaker),
    comparing two consecutive elements and swapping them if the previous element
    is larger than the next element, until no swaps have been made.

    Sources:
        https://www.geeksforgeeks.org/dsa/cocktail-sort/
        https://en.wikipedia.org/wiki/Cocktail_shaker_sort

    Expected results:
        Best Case O(n)
        Average Case O(n^2)
        Worst Case O(n^2)

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        array (list[int]): The unsorted array of integers to be sorted.

    Returns:
        AlgorithmReport: containing a sorted array and the number of comparisions used.

    Author: TheodoreT
    """
    arrayCopy = array.copy()
    report = AlgorithmReport(arrayCopy, 0)
    swapPerformed = True
    arrayLength = len(arrayCopy)
    startIndex = 0
    endIndex = arrayLength - 1

    while swapPerformed == True:
        swapPerformed = False
        for i in range(startIndex, endIndex):
            if arrayCopy[i] > arrayCopy[i + 1]:
                arrayCopy[i], arrayCopy[i + 1] = arrayCopy[i + 1], arrayCopy[i]
                swapPerformed = True
            report.numberOfComparisions += 1
        if swapPerformed == False:
            break
        endIndex = endIndex - 1

        swapPerformed = False
        for i in range(endIndex - 1, startIndex - 1, -1):
            if arrayCopy[i] > arrayCopy[i + 1]:
                arrayCopy[i], arrayCopy[i + 1] = arrayCopy[i + 1], arrayCopy[i]
                swapPerformed = True
            report.numberOfComparisions += 1
        if swapPerformed == False:
            break
        startIndex = startIndex + 1

    return report


def heapsort(array: list[int]) -> AlgorithmReport:
    """
    TODO MAKE SURE COUNTING IS CORRECT

    Sorts an array of integers using the heapsort algorithm.

    Sources:
        https://www.geeksforgeeks.org/dsa/heap-sort/
        https://algs4.cs.princeton.edu/24pq/

    Expected results:
        All cases: O(n log n)

    Requirements:
        Count only element-to-element comparisons that determine ordering,
        (e.g., a[i] < a[j]). Do not count loop bounds checks or index comparisons.

    Args:
        array (list[int]): The unsorted array of integers to be sorted.

    Returns:
        AlgorithmReport: containing a sorted array and the number of comparisions used.

    Author: TheodoreT
    """

    def heapify(report: AlgorithmReport, n, i):
        largest = i
        leftChildIndex = 2 * i + 1
        rightChildIndex = 2 * i + 2

        if leftChildIndex < n and report.sortedArray[leftChildIndex] > report.sortedArray[largest]:
            largest = leftChildIndex
        if rightChildIndex < n and report.sortedArray[rightChildIndex] > report.sortedArray[largest]:
            largest = rightChildIndex
        report.numberOfComparisions += 2

        if largest != i:
            report.sortedArray[i], report.sortedArray[largest] = report.sortedArray[largest], report.sortedArray[i]
            heapify(report, n, largest)

        report.numberOfComparisions += 1

    def sortDown(report: AlgorithmReport):
        arrayLength = len(report.sortedArray)

        for i in range(arrayLength // 2 - 1, -1, -1):
            heapify(report, arrayLength, i)

        for i in range(arrayLength - 1, 0, -1):
            report.sortedArray[0], report.sortedArray[i] = report.sortedArray[i], report.sortedArray[0]
            heapify(report, i, 0)

    report = AlgorithmReport(array.copy(), 0)
    sortDown(report)
    return report
