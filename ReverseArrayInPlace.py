def reverse_array_short(arr):
    it = iter(arr)  # Create an iterator
    reversed_arr = list(it)[::-1]  # Convert to list and reverse
    return reversed_arr

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_array_short(array))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def reverse_array_in_place(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n // 2):  # Loop through the first half of the array
        # Swap the elements at index i and n - 1 - i
        temp = arr[i]  # Store the current element
        arr[i] = arr[n - 1 - i]  # Assign the element from the end
        arr[n - 1 - i] = temp  # Assign the stored element to the end
    return arr  # Return the reversed array

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_array_in_place(array))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# shortest way
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]  # This will create a new list: [5, 4, 3, 2, 1]
print(reversed_arr)