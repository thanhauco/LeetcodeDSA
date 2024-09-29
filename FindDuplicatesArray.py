def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# Example usage
array = [1, 2, 3, 4, 2, 5, 3]
print(find_duplicates(array))  # Output: [2, 3]