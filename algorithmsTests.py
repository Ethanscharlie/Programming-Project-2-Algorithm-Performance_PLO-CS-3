"""
Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran
CS 2430 Team 6
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026
Primary author: Christian Miller
"""

import algorithms
from algorithms import AlgorithmReport

def testDriver(n : int) -> list[AlgorithmReport]:
    """
    driver program that calls your functions from Part 2 and the generator from Part 1. 
    Then runs all four algorithms on each permutation, and records:

    Returns:
        Algorithm name

        The unsorted array used

        Number of comparisons
    
    """
    #TODO UPDATE COMMENT (I can do this, don't do it for me)
    #TODO IMPLEMENT
    algorithms.generateArrayOfAllPossiblePermutations(n) #is there a better name for this?


    return None
    pass

def experimentalRuns():
    """
    Run your system for n = 4, 6, 8 and record for each algorithm:

    Best 10 cases (fewest comparisons) and the input arrays that produced them

    Worst 10 cases (most comparisons) and the input arrays that produced them
        
    Average comparisons across all permutations

    """
    #TODO UPDATE COMMENT (I can do this, don't do it for me)
    #TODO IMPLEMENT

    testDriver(4)
    testDriver(6)
    testDriver(8)

    pass

if __name__=="__main__":
    experimentalRuns()