def find_missing_number(arr):
    n = len(arr) + 1  # The expected length of the array (including the missing number)
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = sum(arr)  # Sum of the given array
    missing_number = expected_sum - actual_sum  # Calculate the missing number
    return missing_number

# Example usage
array = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(find_missing_number(array))  # Output: 5

def find_two_missing_numbers(arr):
    n = len(arr) + 2  # The expected length of the array (including two missing numbers)
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = sum(arr)  # Sum of the given array
    missing_sum = expected_sum - actual_sum  # Sum of the two missing numbers
    
    # Find the average of the missing numbers
    average_missing = missing_sum // 2
    
    # Partition the array and the range 1..n into two parts:
    # Numbers <= average_missing and numbers > average_missing
    sum_small = sum(x for x in arr if x <= average_missing)
    expected_sum_small = sum(range(1, average_missing + 1))
    
    # The first missing number is in the smaller half
    first_missing = expected_sum_small - sum_small
    
    # The second missing number is the difference between the sum of missing numbers and the first missing number
    second_missing = missing_sum - first_missing
    
    return first_missing, second_missing

# Example usage
array = [1, 2, 4, 5, 6, 7, 8, 10]  # 3 and 9 are missing
print(find_two_missing_numbers(array))  # Output: (3, 9)

# time complexity: O(n)
# space complexity: O(1)



