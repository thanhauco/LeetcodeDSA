
def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    left = 0
    longest_substring = ""  # Initialize variable to store the longest substring

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1  # Move left pointer past the duplicate

        char_index[s[right]] = right  # Update the last seen index of the character
        current_length = right - left + 1  # Calculate current length
        if current_length > max_length:  # Check if current length is greater than max_length
            max_length = current_length
            longest_substring = s[left:right + 1]  # Update longest_substring

    return max_length, longest_substring  # Return both length and substring

# Example usage:
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: (3, "abc")

s = "adsfsdsfsf"
print(length_of_longest_substring(s))  # Output: (4, "sdsf")