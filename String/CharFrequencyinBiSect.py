def char_frequency(sorted_string, char):
    from bisect import bisect_left, bisect_right
    
    # Find the leftmost occurrence of `char`
    left_index = bisect_left(sorted_string, char)
    # Find the rightmost occurrence of `char`
    right_index = bisect_right(sorted_string, char) - 1
    
    # If the character is not found, return 0
    if left_index >= len(sorted_string) or sorted_string[left_index] != char:
        return 0
    
    # Frequency is the difference of indices + 1
    return right_index - left_index + 1

# Example usage:
sorted_string = "aaabbbccccccceeee"
char = 'c'
print(char_frequency(sorted_string, char))  # Output: 7

# Don't use bisect module
def char_frequency_2(sorted_string, char):
    def find_leftmost(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  # Returns the index of the first occurrence

    def find_rightmost(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right  # Returns the index of the last occurrence

    # Perform the searches
    left_index = find_leftmost(sorted_string, char)
    right_index = find_rightmost(sorted_string, char)

    # If the character is not present
    if left_index >= len(sorted_string) or sorted_string[left_index] != char:
        return 0

    # Frequency is right_index - left_index + 1
    return right_index - left_index + 1

# Example usage:
sorted_string = "aaabbbccccccceeee"
char = 'c'
print(char_frequency_2(sorted_string, char))  # Output: 7