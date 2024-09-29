from collections import Counter

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


def count_duplicates(arr):
    seen = set()
    duplicates = set()
    counts = {}  # dictionary to count occurrences
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
            counts[item] += 1  # Increment count for duplicates
        else:
            seen.add(item)
            counts[item] = 1  # Initialize count for new items
    
    # I want to return count but with items occurence > 1
    return {item: count for item, count in counts.items() if count > 1}

# Example usage
array = [0, 2, 3, 4, 2, 5, 3, 5, 2, 1, 4]
print(count_duplicates(array))  # output: {2: 3, 3: 2, 4: 2, 5: 2}


# Using Counter class faster
def find_duplicates_Counter(arr):
    counts = Counter(arr)
    return [item for (item, count) in counts.items() if count > 1]

# Example usage
array = [1, 2, 3, 4, 2, 5, 3]
print(find_duplicates(array))  # Output: [2, 3]