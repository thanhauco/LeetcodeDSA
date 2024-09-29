def find_missing_number(arr):
    n = len(arr) + 1  # The expected length of the array (including the missing number)
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = sum(arr)  # Sum of the given array
    missing_number = expected_sum - actual_sum  # Calculate the missing number
    return missing_number

# Example usage
array = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(find_missing_number(array))  # Output: 5

# time complexity: O(n)
# space complexity: O(1)

