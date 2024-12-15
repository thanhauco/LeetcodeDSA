# Array/SmallestSubarraywithSumGreaterthanorEqualtoTarget.py
"""
Given an array of positive integers arr and a target sum target, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to target. 
If no such subarray exists, return 0.
"""

def smallest_subarray_with_sum(arr, target):
    start = 0
    window_sum = 0
    min_length = float('inf')
    min_subarray = []

    for end in range(len(arr)):
        # Add the current element to the window
        window_sum += arr[end]

        # Shrink the window while the condition is satisfied
        while window_sum >= target:
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_subarray = arr[start:end + 1]  # Capture the subarray
            window_sum -= arr[start]
            start += 1

    return (min_length, min_subarray) if min_length != float('inf') else (0, [])

# Example usage
arr = [2, 3, 1, 2, 4, 3]
target = 7
result_length, result_subarray = smallest_subarray_with_sum(arr, target)
print(f"The length of the smallest subarray is: {result_length}, Subarray: {result_subarray}")  # Output: 2, Subarray: [4, 3]

arr = [1, 4, 4]
target = 4
result_length, result_subarray = smallest_subarray_with_sum(arr, target)
print(f"The length of the smallest subarray is: {result_length}, Subarray: {result_subarray}")  # Output: 1, Subarray: [4]

arr = [1, 1, 1, 1, 1, 1]
target = 11
result_length, result_subarray = smallest_subarray_with_sum(arr, target)
print(f"The length of the smallest subarray is: {result_length}, Subarray: {result_subarray}")  # Output: 0, Subarray: []