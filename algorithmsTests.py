"""
Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran
CS 2430 Team 6
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026
Primary author: Christian Miller
"""

import algorithms
from algorithms import AlgorithmReport
from collections.abc import Callable
from dataclasses import dataclass

@dataclass
class TestReport:
    unsortedArray : list[int]
    numberOfComparisions : int

permutations = {
    4 : algorithms.generateArrayOfAllPossiblePermutations(4),
    6 : algorithms.generateArrayOfAllPossiblePermutations(6),
    8 : algorithms.generateArrayOfAllPossiblePermutations(8)
}

def alreadySortedList(n : int) -> list[int]:
    """
    Creates a list of length n which is the same as a sorted list from algorithms.py.

    For Example, if n = 3, this function returns {0, 1, 2}

    Returns:
        list[int]: A list containing all integers from 0 to n
    
    Author: Christian Miller
    """
    assert n > 0

    output : list[int] = []
    for i in range(n):
        output.append(i)
    return output

def testDriver(n : int, algorithm : Callable) -> list[TestReport]:
    """
    A program which retrieves the permutations generated from 
    algorithms.generateArrayOfAllPossiblePermutations
    Then performs a sorting algorithm on each.

    Args:
        n (int): The size of the permutation arrays
        algorithm (Callable): The sorting algorithm to perform on each permutation.

    Returns:
        list[TestReport]: A list containing, for each permutation,
        the number of comparisons and unsorted array given as input.
    
    Author: Christian Miller
    """
    
    lists = permutations[n]

    output : list[TestReport] = []

    for i in range(n):

        currentList = lists[i]
        permutation : AlgorithmReport = algorithm(currentList)

        assert permutation.sortedArray == alreadySortedList(n)

        output.append(TestReport(currentList, permutation.numberOfComparisions))

    return output
    pass

def run(algorithm : Callable, name : str):
    """
    calls TestDriver for n = 4, 6, 8 for each algorithm. Records
    the 10 cases with the fewest comparisons, the 10 cases with the most comparisons,
    and the average comparisons across all permutations, printing each to console.

    Args:
        algorithm (Callable): The sorting algorithm to use for each case.
        name (str): The name of the sorting algorithm to be printed to console.

    Author: Christian Miller
    """

    runs = testDriver(4, algorithm)
    runs += testDriver(6, algorithm)
    runs += testDriver(8, algorithm)
    
    best = runs.copy()
    worst = runs.copy()
    best.sort(key=lambda x: x.numberOfComparisions, reverse=False)
    worst.sort(key=lambda x: x.numberOfComparisions, reverse=True)

    #Get Average
    sum = 0
    for i in range(len(runs)):
        sum += runs[i].numberOfComparisions
    averageRuns = sum/len(runs)

    print(name + " Results: ")
    print("")
    #best
    print("10 best results: ")
    print("")
    print10(best)
    #worst
    print("10 worst results: ")
    print10(worst)
    print("Average Runs: " + str(averageRuns))
    print("")

def experimentalRuns():
    """
    Runs tests for four sorting algorithms: 
    mergesort, quicksort, shakersort, and heapsort.

    Author: Christian Miller
    """

    run(algorithms.mergesort, "Merge Sort")
    run(algorithms.quicksort, "Quick Sort")
    run(algorithms.shakerSort, "Shaker Sort")
    run(algorithms.heapsort, "Heap Sort")

def print10(listOfResults : list[TestReport]):
    """
    Takes the first ten entries in a list[TestReport], printing
    the unsorted array used and the number of comparisons in it.

    Args:
        listOfResults (list[TestReport]): A list of test results to print to the console,
        containing an unsorted array and the number of comparisons used in the sorting algorithm. 
    """
    for i in range(len(listOfResults[:10])):
        print(str(i+1) + ": ")
        print("n = " + str(len(listOfResults[i].unsortedArray)) + ", unsorted array: " + str(listOfResults[i].unsortedArray))
        print("number of comparisons: " + str(listOfResults[i].numberOfComparisions))
    print("")

if __name__=="__main__":
    experimentalRuns()