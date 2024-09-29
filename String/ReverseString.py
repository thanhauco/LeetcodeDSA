def reverse_string(s):
    return s[::-1]

# 2 pointer approach
def reverse_string_in_place(s):
    # Convert string to list of characters (strings are immutable in Python)
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)

# Example usage
original_string = "Hello, World!"
print("Original string:", original_string)

reversed_string = reverse_string(original_string)
print("Reversed string (using slicing):", reversed_string)

reversed_in_place = reverse_string_in_place(original_string)
print("Reversed string (in-place):", reversed_in_place)
