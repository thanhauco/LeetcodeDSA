def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

# Example usage
array = [3, 5, 1, 2, 4, 8]
max_val, min_val = find_max_min(array)
print("Maximum value:", max_val)  # Output: 8
print("Minimum value:", min_val)  # Output: 1


# time complexity: O(n)
# space complexity: O(1)
