# Programming-Project-2-Algorithm-Performance_PLO-CS-3
Implement multiple sorting algorithms, generate input data systematically, and measure performance using a consistent metric (number of comparisons)

To run:
Download and extract the .zip file into a folder.

Run algorithmsTests.py in the Command Prompt or Python Interpreter of choice.

# algorithms.py
- Part 1:
  - Generates all possible permutations of the integers 0 through n − 1 for a given small n.
- Part 2:
  - Implements the following four sorting algorithms:
    - Mergesort
    - Quicksort
    - Shaker sort (bidirectional bubble)
    - Heapsort
  - Each algorithm:
    - Accepts an unsorted array of integers as input.
    - Returns or make available the sorted array.
    - Counts and reports the number of comparisons performed.


# algorithmsTests.py
- Part 3:
  - Calls the functions from Part 2 and the generator from Part 1. Then runs all four algorithms on each permutation, and records:
    - Algorithm name
    - The unsorted array used
    - Number of comparisons

- Part 4:
  - Runs system for n = 4, 6, 8 and records for each algorithm:
    - Best 10 cases (fewest comparisons) and the input arrays that produced them.
    - Worst 10 cases (most comparisons) and the input arrays that produced them.
    - Average comparisons across all permutations.
