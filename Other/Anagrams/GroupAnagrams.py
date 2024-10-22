from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        # Sort the string and use it as a key
        key = tuple(sorted(s))
        anagram_map[key].append(s)

    # Convert the values of the dictionary to a list
    return list(anagram_map.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]