Ethan J. Hadley, Chris Miller, Christopher Reynolds, and Theodore Tran
CS 2430 Section 502 Team 6
Programming Project 2: Algorithm Performance_PLO-CS-3 Spring 2026
Primary author: Theodore Tran


# Part 1 Array Generator 

```
generateArrayOfAllPossiblePermutations (int n)
{

# Stage 1: create the array of the given size

# Current Implementation:
# Create an array of size n.

# Theodore's Previous Draft:
# Creates the "set" array that contains all the numbers
universal_set = list() 
# For loop appends integer n and increments n each iteration. Iterate this n times, starting with n = 0.
for (int i; i < n; i++) universal_set.append(i)


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

# recursively cut the array in half until there's only subgroups of 1
# then, for each recursion, take two subgroups and "merge" them by comparing values of each subgroup until there are no more values in both subgroups.

}

quicksort (int array[]) 
{

# make the pivot (starting from the first element) 
# then find the "true" position of the pivot by going through the array. 
# Compare and swap the pivot with the next element until ALL elements on the left side of the pivot are less than the pivot, and all of the elements on the right side of the pivot are greater than the pivot
# after the pivot is placed in its "true" position, cut the groups by the pivot. 
# then recursively call this function until each pivot is in its "true" position.

}

shakerSort(int array[])
{
# a.k.a. Bidirectional Bubble Sort/Cocktail Sort
# Sources: 
# https://www.geeksforgeeks.org/dsa/cocktail-sort/
# https://en.wikipedia.org/wiki/Cocktail_shaker_sort

# "array" is the name of the local variable.
    arrayCopy = array.copy() # Creates a copy of the array, which the copy will be sorted.
    report = AlgorithmReport(arrayCopy, 0) # Creates the report to be returned.
    # Keeps track of any swaps that occur to know when to stop the while loop.
    # True means at least one swap was performed, 
    # False means no swaps were performed.
    swapPerformed = True 
    # Gets and stores the beginning and end indices of the array.
    # These are used to know when to stop "going through the array".
    arrayLength = len(arrayCopy) 
    startIndex = 0
    endIndex = arrayLength - 1

# Loop Stages 1 & 2 until no swaps are performed in either Stage 1 or Stage 2.
   	 while (swapPerformed == True):
        	# Resets swapPerformed to False in case it was True in a previous iteration.
        	swapPerformed = False

# Stage 1: loop through array from left to right.
# during loop, two adjacent items are compared. If the value on the left is greater than the value on the right, then the values are swapped. Else, do nothing to that pair.
# After the loop gets to the end of the array, the largest number will be at the end of the array.
        for i in range(startIndex, endIndex):
            # Checks if current element is bigger than next element.
            if (arrayCopy[i] > arrayCopy[i + 1]):
                # Swaps bigger current element with the smaller next element.
                arrayCopy[i], arrayCopy[i + 1] = arrayCopy[i + 1], arrayCopy[i]
                swapPerformed = True # Marks that a swap has been performed.
            report.numberOfComparisons += 1 # Counts comparison.
        # If a swap was not performed, that means array is sorted and while loop can end.
        if (swapPerformed == False): break
        # Largest number is now at the end of the array after loop, 
        # so we no longer need to sort that element from now on.
        endIndex = endIndex - 1

        # Resets swapPerformed to False in case it was True in the previous stage.
        swapPerformed = False

# Stage 2: loop through array backwards from right to left.
# start loop with the pair right before the last element in the array.
# during loop, two adjacent items are compared. If the value on the left is greater than the value on the right, then the values are swapped. Else, do nothing to that pair.
# After the loop gets to the start of the array, smallest item will be at the beginning of the array.

        # Both startIndex and endIndex need to be subtracted by 1 so that 
        # the pair of elements being compared can be i and i+1, 
        # since i-1 at i=0 does not work (out of bounds).
        for i in range(endIndex - 1, startIndex - 1, -1):
            # Checks if current element is bigger than next element.
            if (arrayCopy[i] > arrayCopy[i + 1]):
                # Swaps bigger current element with the smaller next element.
                arrayCopy[i], arrayCopy[i + 1] = arrayCopy[i + 1], arrayCopy[i]
                swapPerformed = True # Marks that a swap has been performed.
            report.numberOfComparisons += 1 # Counts comparison.
        # If a swap was not performed, that means array is sorted and while loop can end.
        if (swapPerformed == False): break
        # Smallest number is now at the beginning of the array after loop, 
        # so we no longer need to sort that element from now on.
        startIndex = startIndex + 1
    
    return report

}

heapsort(int array[])
{
# Sources: 
# https://www.geeksforgeeks.org/dsa/heap-sort/
# https://algs4.cs.princeton.edu/24pq/

# <-- Algs 4 Implementation --> 
    # // The only problem is that this implementation may not work with standard arrays and only works with priority queues. Not sure.
    # Store length of pq in n
    arrayLength = len(arrayCopy)

    # Phase 1: Heapify; Heap Construction
    # //root is at 0 in the heap
    # for (int k = n // 2 ; k >= 1; k--) // k starts in the middle of heap, k ends at index 1 (which is the index after the root)
    for parentIndex in range(arrayLength//2, 1, -1)
	    # sink(pq, k, n)
	    sink(arrayCopy, parentIndex, arrayLength)

    # Phase 2: Sortdown
    # int k = n
    k = arrayLength
    # while (k > 1)
    while (currentIndex > 1)
	    # swap element at index 1 with element at index k
	    arrayCopy[1], arrayCopy[k] = arrayCopy[k], arrayCopy[1]
	    # decrement k
	    k-=1
	    # sink (pq, 1, k)
	    sink(arrayCopy, 1, k)

    # Sink Function
    # void sink(pq, k, n) // k is the index of the parent
    def sink(array: int[], parentIndex: int, heapLength: int)
	    # // This loop looks for the largest element between k and these j's, and swaps until k is the largest element out of them all
	    # while (2 * k <= n) // n is length of entire array
	    while (2 * parentIndex <= heapLength)
		    # int j = 2 * k // j is the index of the left child, j+1 is right child
		    childIndex = 2 * parentIndex
		    # if (j < n && (/* j is less than j+1 */) ) # index j must be inside of the array
		    if (childIndex < heapLength && (childIndex < childIndex + 1)):
			    # increment j //increment is to compare j+1 and k, rather than comparing j and k
			    childIndex+=1
		    # if (/* k is NOT less than j */) break out of loop // this means k is the largest number between these elements
		    if (parentIndex >= childIndex): break
		    # // Otherwise, k is less than J, so J should be the parent and should be checked again.
			# swap K and J
		    arrayCopy[parentIndex], arrayCopy[childIndex] = arrayCopy[childIndex], arrayCopy[parentIndex]

# Code
	def sink(report: AlgorithmReport, array: list[int], parentIndex: int, heapLength: int):
        	while (2 * parentIndex <= heapLength):
            		childIndex = 2 * parentIndex
            		if (childIndex < heapLength and (array[childIndex] < array[childIndex + 1])): childIndex += 1
            		report.numberOfComparisons += 1
            		if (array[parentIndex] >= array[childIndex]): 
                		report.numberOfComparisons += 1
                		break
            		report.numberOfComparisons += 1
            		array[parentIndex], array[childIndex] = array[childIndex], array[parentIndex]

    	arrayCopy = array.copy()
    	report = AlgorithmReport(arrayCopy, 0)
    	arrayLength = len(arrayCopy)

    	for parentIndex in range(arrayLength // 2, 1, -1): 
        	sink(report, arrayCopy, parentIndex, arrayLength)
    
    	currentIndex = arrayLength
    	while (currentIndex > 1):
        	arrayCopy[1], arrayCopy[currentIndex] = arrayCopy[currentIndex], arrayCopy[1]
        	currentIndex -= 1
        	sink(report, arrayCopy, 1, currentIndex)
    
    	return report
		

# <-- GeeksForGeeks Implementation -->
    # Heapify an array all at once
    def heapify(givenArray, numberOfElements, currentIndex): 
	    # largest number (current Index) is the root of the created heap
	    # left child; root's left branch's index 2i+1 (every element to the left is at an odd index)
	    # right child; root's right branch's index is 2i+2 (every element to the right is at an even index)
	
	    # If left child is larger than the root, then switch the child and the root
	    # If right child is larger than the root, then switch the child and the root
	    # If largest is not the root, 

    # Max Heap; all smaller elements swim up by swapping places
    def heapsort(givenArray):
	    # get and store Number of Elements into n
	    # for each element before the middle of heap, heapify
		    # middle of heap: half of n and subtract by 1
		    # end at -1
		    # decrement
	    # for each element in the heap, (looping through from the second to last element to the first element)
		    # swap the current root of the heap (largest number) to the current index (the actual position)
		    # heapify again, but this time with the current largest number as the root


    # Other Notes

    # <-- Stage 1: Treat Array as a Complete Binary Tree -->
	    # array of size n
	    # root is at index 0
	    # every element to the left is at an odd index (2i + 1)
	    # every element to the right is at an even index (2i + 2)

    # <-- Stage 2: Build Max Heap -->
    # Parent nodes are larger than Child Nodes

    # <-- Stage 3: Sort Array -->
    # Sort the Array by placing Largest Element at the End of Unsorted Array.

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
# Just brainstorming here, but maybe a solution could be to have the driver() function handle outputting the original list
```


# Part 4 Experimental Runs and Data Collection 
```
driver(4)
driver(6)
driver(8)
```
