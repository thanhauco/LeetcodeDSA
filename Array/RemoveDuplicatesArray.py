def remove_duplicates(arr):
    return list(set(arr))

# Example usage
array = [1, 2, 3, 4, 2, 5, 3]
print(remove_duplicates(array))  # Output: [1, 2, 3, 4, 5]

# Another way to remove duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
[unique_list.append(item) for item in my_list if item not in unique_list]
print(unique_list)  # Output: [1, 2, 3, 4, 5]


# time complexity: O(n)
# space complexity: O(n)

