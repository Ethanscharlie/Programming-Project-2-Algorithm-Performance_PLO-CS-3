Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran
CS 2430 Section 502 Team 6
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026
Primary author: Theodore Tran

## Data Structures Used
- Python Lists
- ```AlgorithmReport``` class
  - sortedArray: list[int]
  - numberOfComparisions: int

# Invariants
- Count only element-to-element comparisons that determine ordering, (e.g., ```a[i] < a[j]```). Do not count loop bounds checks or index comparisons.

# Assumptions
- When using the ```driver()``` function, only integers are inputted. Any other input is invalid (ex. "one", "1.1", etc. are invalid inputs).

# Tradeoffs
- Adapted the implementations from other sources rather than implementing entire algorithms from scratch to increase production speed and convenience at the cost of needing to document based on those implementations (instead of documenting alongside implementation).

# Other Design Notes and Decisions
- Will the functions themselves keep track of how many comparisons it makes? Or is there some way for the “driver program” to obtain that data? 
  - The sorting functions themselves will keep track or “report” the number of comparisons. The variable ```AlgorithmReport``` will contain both the sorted array and the information.
- Will the functions sort the given array directly or will they need to copy the array first and then sort the copy?
  - In the current implementation, functions directly sort the given array, rather than copying the given array.
