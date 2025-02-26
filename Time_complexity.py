"""
Time Complexity in Python

Time complexity refers to the computational complexity that describes the amount of time an algorithm takes to run as a function of the length of the input. Below are common time complexities with examples.
"""

# 1. O(1) - Constant Time Complexity
# The execution time does not depend on the input size.
def constant_time(arr):
    """Returns the first element of the array in O(1) time"""
    return arr[0] if arr else None

# Example:
arr = [10, 20, 30]
print("O(1) Example:", constant_time(arr))


# 2. O(n) - Linear Time Complexity
# The execution time grows linearly with the input size.
def linear_time(arr):
    """Prints each element in O(n) time"""
    for num in arr:
        print(num)

# Example:
print("\nO(n) Example:")
linear_time(arr)


# 3. O(n^2) - Quadratic Time Complexity
# The execution time grows exponentially with input size.
def quadratic_time(arr):
    """Compares each element with every other element in O(n^2) time"""
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(f"Comparing {arr[i]} and {arr[j]}")

# Example:
print("\nO(n^2) Example:")
quadratic_time(arr)


# 4. O(log n) - Logarithmic Time Complexity
# The execution time increases logarithmically.
def logarithmic_time(n):
    """Reduces n by half each iteration, O(log n) time"""
    while n > 1:
        print(n)
        n //= 2

# Example:
print("\nO(log n) Example:")
logarithmic_time(16)


# 5. O(n log n) - Linearithmic Time Complexity
# Common in efficient sorting algorithms like Merge Sort
import random

def merge_sort(arr):
    """Sorts the array using Merge Sort in O(n log n) time"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Merges two sorted lists"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example:
random_arr = [random.randint(1, 100) for _ in range(10)]
print("\nO(n log n) Example:")
print("Unsorted:", random_arr)
print("Sorted:", merge_sort(random_arr))


# 6. O(2^n) - Exponential Time Complexity
# The execution time doubles with each increase in input size.
def exponential_time(n):
    """Computes Fibonacci recursively in O(2^n) time"""
    if n <= 1:
        return n
    return exponential_time(n-1) + exponential_time(n-2)

# Example:
print("\nO(2^n) Example:")
print("Fibonacci(5):", exponential_time(5))


# 7. O(n!) - Factorial Time Complexity
# Very slow growth, used in brute force solutions.
def factorial_time(n):
    """Finds all permutations of n elements in O(n!) time"""
    from itertools import permutations
    perm = list(permutations(range(n)))
    print("Total permutations:", len(perm))

# Example:
print("\nO(n!) Example:")
factorial_time(4)

