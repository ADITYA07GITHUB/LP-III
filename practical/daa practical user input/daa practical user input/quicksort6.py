##determinstic quicksort

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

quick_sort(arr, 0, n - 1)

print("Deterministic Sorted array:", arr)
###time complexity of quicksort is O(nlogn) and space complexity is O(logn)

##randomized quicksort

import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        r = random.randint(low, high)
        arr[r], arr[high] = arr[high], arr[r]

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

quick_sort(arr, 0, n - 1)

print(" Randomized Sorted array:", arr)

###time complexity of randomized quicksort is O(nlogn) and space complexity is O(logn)



# Line-by-line explanation
# Part A: Partition function
# Line 1:
# def partition(arr, low, high):



# This function divides the array around a pivot.
# - arr = Our array
# - low = Starting index
# - high = Ending index
# Line 2:
# pivot = arr[high]



# Selects the last element as the pivot.

# Example:
# Array = [5, 3, 8, 4, 2]
# Pivot = 2


# Line 3:
# i = low - 1



# i tracks the last position containing an element smaller than or equal to the pivot.

# Initially, i = -1 when low = 0.

# Line 4:
# for j in range(low, high):



# This loop checks every element except the pivot.

# Line 5:
# if arr[j] <= pivot:



# Checks whether the current element is smaller than or equal to the pivot.

# Lines 6–7:
# i += 1arr[i], arr[j] = arr[j], arr[i]



# If the condition is true, increase i and swap the elements.

# Lines 8–9:
# arr[i + 1], arr[high] = arr[high], arr[i + 1]return i + 1



# Places the pivot in its correct sorted position and returns that index.
# Part B: Quick Sort function
# def quick_sort(arr, low, high):



# Defines the recursive sorting function.
# if low < high:



# Checks whether the current part contains at least two elements.
# pi = partition(arr, low, high)



# Calls the partition function and stores the pivot index in pi.
# quick_sort(arr, low, pi - 1)



# Sorts elements to the left of the pivot.
# quick_sort(arr, pi + 1, high)



# Sorts elements to the right of the pivot.
# Part C: User input
# n = int(input("Enter number of elements: "))



# Takes the number of elements from the user.
# arr = []



# Creates an empty list.
# for i in range(n):    num = int(input("Enter element: "))    arr.append(num)



# Takes each element and adds it to the list.
# quick_sort(arr, 0, n - 1)



# Calls Quick Sort for the complete array.
# print("Sorted array:", arr)



# Displays the sorted array.

# 3. Dry run of Deterministic Quick Sort
# Let's sort [5, 3, 8, 4, 2].
# Quick Sort Visualization

# Step 1 of 5

# 5

# [0]
# 3

# [1]
# 8

# [2]
# 4

# [3]
# 2

# Pivot

# Choose the last element, 2, as the pivot.
#  PreviousNext 


# 4. Randomized Quick Sort – Python
# import randomdef partition(arr, low, high):    pivot = arr[high]    i = low - 1    for j in range(low, high):        if arr[j] <= pivot:            i += 1            arr[i], arr[j] = arr[j], arr[i]    arr[i + 1], arr[high] = arr[high], arr[i + 1]    return i + 1def quick_sort(arr, low, high):    if low < high:        r = random.randint(low, high)        arr[r], arr[high] = arr[high], arr[r]        pi = partition(arr, low, high)        quick_sort(arr, low, pi - 1)        quick_sort(arr, pi + 1, high)n = int(input("Enter number of elements: "))arr = []for i in range(n):    num = int(input("Enter element: "))    arr.append(num)quick_sort(arr, 0, n - 1)



# What changes in Randomized Quick Sort?
# Only three important lines need special attention.

# Line 1:
# import random



# Imports Python's random module to generate random numbers.

# Line 2:
# r = random.randint(low, high)



# Selects a random index between low and high, including both endpoints.

# Example: If low = 0 and high = 4, it may select index 2.

# Line 3:
# arr[r], arr[high] = arr[high], arr[r]



# Swaps the randomly selected element with the last element.

# After this, the normal partition() function is called.

# All remaining steps are the same as deterministic Quick Sort.

# 5. Time complexity explanation for viva
# Case	Time complexity	Reason
# Best	O(n log n)	Pivot divides the array into nearly equal parts
# Average	O(n log n)	Partitions are reasonably balanced overall
# Worst	O(n²)	Pivot repeatedly creates highly unbalanced partitions

# Randomized Quick Sort has expected O(n log n) time complexity, although its worst case remains O(n²).
# Why O(n log n)?
# - n: Each partitioning level processes a total of approximately n elements.
# - log n: Balanced partitions create approximately log n levels.
# Therefore:
# \[
# O(n)\times O(\log n)=O(n\log n)
# \]

# 6. How to explain the code to your examiner
# Sir/Madam, this program implements Quick Sort using Divide and Conquer. First, we select a pivot element. The partition function places smaller elements on the left and larger elements on the right. Then Quick Sort recursively sorts both parts. In deterministic Quick Sort, we select the last element as pivot. In randomized Quick Sort, we select a random pivot. The average time complexity is O(n log n), and the worst-case complexity is O(n²).

# Most important viva question: Why do we use i = low - 1?

# Answer: Because initially, we have not found any element smaller than or equal to the pivot. As we find such elements, we increase i and place them on the left side.