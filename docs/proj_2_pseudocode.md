Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran  
CS 2430 Team 6  
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026  
Primary author: Theodore Tran  


# Part 1 Array Generator 

```
generateArrayOfAllPossiblePermutations (int n)
{

# Stage 1: create the array of the given size

# Current Implementation:
# Create an array of size n.

# Theodore's Previous Draft of Stage 1:
{
  # Creates the "set" array that contains all the numbers
  universal_set = list() 
  # For loop appends integer n and increments n each iteration. Iterate this n times, starting with n = 0.
  for (int i; i < n; i++) universal_set.append(i)
}


# Stage 2: use lexicographic permutation algorithm to create all permutations 
# Create an auxiliaryArray that is a copy of the original array.
# For each index of both arrays, loop the following until i >= n:
{
  # if the current index is the same as the value of the current index of the auxiliaryArray, set the value of the current index to 0. Increment the index. Skip the rest of the loop and move onto the next loop.
  # if the current index is even, use tuple unpacking to swap the values of the first index and the current index in the original array.
  # if the current index is odd, use tuple unpacking to swap the values at the current index of both arrays.
  # Append the current state of the array (one of the permutations) into the output array.
  # Increment the value in the current index of the auxiliaryArray.
  # Set the index to 1.
}
# return the output array, which contains all the permutations.

}
```



# Part 2 Implement Sorting Algorithms
Each "sort" function counts/reports number of comparisons performed in the console once and returns the sorted array.

```
mergesort (int array[])
{
# WIP
# recursively cut the array in half until there's only subgroups of 1
# then, for each recursion, take two subgroups and "merge" them by comparing values of each subgroup until there are no more values in both subgroups.
}

quicksort (int array[]) 
{
# WIP
# make the pivot (starting from the first element) 
# then find the "true" position of the pivot by going through the array. 
# Compare and swap the pivot with the next element until ALL elements on the left side of the pivot are less than the pivot, and all of the elements on the right side of the pivot are greater than the pivot
# after the pivot is placed in its "true" position, cut the groups by the pivot. 
# then recursively call this function until each pivot is in its "true" position.
}

shakerSort(int array[])
{
# a.k.a. Bidirectional Bubble Sort/Cocktail Sort
# Source: https://www.geeksforgeeks.org/dsa/cocktail-sort/

# Loop Stages 1 & 2 until no swaps are performed in either Stage 1 or Stage 2. 

# Stage 1: loop through array.
# during loop, two adjacent items are compared. If the value on the left is greater than the value on the right, then the values are swapped. Else, do nothing to that pair.
# After the loop gets to the end of the array, the largest number will be at the end of the array.

# Stage 2: loop through array backwards.
# start loop with the pair right before the last element in the array.
# during loop, two adjacent items are compared. If the value on the left is greater than the value on the right, then the values are swapped. Else, do nothing to that pair.
# After the loop gets to the start of the array, smallest item will be at the beginning of the array.
}

heapsort(int array[])
{
# WIP
# Heapify an array all at once (add the elements level-by-level)
# Min Heap; all smaller elements swim up by swapping places
}
```



# Part 3 Test Driver and Performance Metrics 

```
driver(some_array[])
{
# Generate permutations from Part 1
# Call all 4 algorithms on each permutation
for permutation in generateArrayOfAllPossiblePermutations(some_array[])
{
  # each function call automatically reports number of comparisons in console?
  print("permutation", permutation)
  print("Merge Sort")
  mergesort(permutation)
  print("Quick Sort")
  quicksort(permutation)
  print("Shaker Sort")
  shakerSort(permutation)
  print("Heap Sort")
  heapsort(permutation)
}
}
```


# Part 4 Experimental Runs and Data Collection 
```
driver(4)
driver(6)
driver(8)
```
