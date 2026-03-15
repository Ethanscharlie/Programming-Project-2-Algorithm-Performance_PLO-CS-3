Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran
CS 2430 Section 502 Team 6
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026
Primary author: Theodore Tran

## Data Structures Used
- Python Lists

# Invariants
- Count only element-to-element comparisons that determine ordering, (e.g., ```a[i] < a[j]```). Do not count loop bounds checks or index comparisons.

# Assumptions
- When using the ```driver()``` function, only integers are inputted. Any other input is invalid (ex. "one", "1.1", etc.).

# Tradeoffs
- Adapted the implementations from other sources rather than implementing entire algorithms from scratch to increase production speed and convenience at the cost of needing to document based on those implementations (instead of documenting alongside implementation).

# Other Design Notes and Decisions
- Will the functions themselves keep track of how many comparisons it makes? Or is there some way for the “driver program” to obtain that data? 
  - The sorting functions themselves will keep track or “report” the number of comparisons. The variable ```report``` of type ```AlgorithmReport``` will contain the information.
