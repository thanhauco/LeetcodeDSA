def are_anagrams(str1, str2):
    # Normalize the strings: convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare the sorted strings
    return sorted_str1 == sorted_str2

# Example usage:
string1 = "Listen"
string2 = "Silent"
print(are_anagrams(string1, string2))  # Output: True