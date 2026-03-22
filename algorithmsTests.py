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

def alreadySortedList(n : int) -> list[int]:
    output : list[int] = []
    for i in range(n):
        output.append(i)
    return output

@dataclass
class TestReport:
    unsortedArray : list[int]
    numberOfComparisions : int

def testDriver(n : int, algorithm : Callable) -> list[TestReport]:
    """
    driver program that calls your functions from Part 2 and the generator from Part 1. 
    Then runs all four algorithms on each permutation, and records:

    Returns:
        Algorithm name

        The unsorted array used

        Number of comparisons
    
    """
    #TODO UPDATE COMMENT (I can do this, don't do it for me)
    
    #lists = algorithms.generateArrayOfAllPossiblePermutations(n) #is there a better name for this?

    output : list[TestReport] = []

    for i in range(n):

        currentList = lists[i]
        permutation : AlgorithmReport = algorithm(currentList)

        assert permutation.sortedArray == alreadySortedList(n)

        output.append(TestReport(currentList, permutation.numberOfComparisions))

    return output
    pass

def run(algorithm : Callable, name : str):

    #MergeSort
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
    print("")
    print10(worst)
    print("Average Runs: " + str(averageRuns))


def print10(listOfResults : list[TestReport]):
    for i in range(len(listOfResults[:10])):
        print(str(i+1) + ": ")
        print("array: " + str(listOfResults[i].unsortedArray))
        print("number of comparisons: " + str(listOfResults[i].numberOfComparisions))
    print("")

def experimentalRuns():
    """
    Run your system for n = 4, 6, 8 and record for each algorithm:

    Best 10 cases (fewest comparisons) and the input arrays that produced them

    Worst 10 cases (most comparisons) and the input arrays that produced them
        
    Average comparisons across all permutations

    """
    #TODO UPDATE COMMENT (I can do this, don't do it for me)

    run(algorithms.mergesort, "Merge Sort")
    run(algorithms.quicksort, "Quick Sort")
    run(algorithms.shakerSort, "Shaker Sort")
    run(algorithms.heapsort, "Heap Sort")
        


if __name__=="__main__":
    experimentalRuns()