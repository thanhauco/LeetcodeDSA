def find_missing_number(arr):
    # Sum of numbers from 1 to 10
    total = 55 # formula n*(n+1)/2
    sum_of_array = sum(arr)  # Sum of the given array
    missing_number = total - sum_of_array  # Calculate the missing number
    return missing_number

# Example usage
array = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(find_missing_number(array))  # Output: 5

# time complexity: O(n)
# space complexity: O(1)

