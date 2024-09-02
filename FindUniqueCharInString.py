def find_unique_chars(s):
    seen = set()
    unique_chars = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            unique_chars.append(char)
    
    return ''.join(unique_chars)

# without using extra space
def find_first_unique_chars_without_extra_space(s):
    for i in range(len(s)):
        found = False
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                found = True
                break
        if not found:
            return s[i]

def find_all_unique_chars_without_extra_space(s):
    unique_chars = []
    
    for i in range(len(s)):
        is_unique = True
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                is_unique = False
                break
        if is_unique:
            unique_chars.append(s[i])
    
    return ''.join(unique_chars)

# Example usage
input_string = "hello world"
result = find_unique_chars(input_string)
print(result)  # Output: "helo wrd"

result = find_first_unique_chars_without_extra_space(input_string)
print(result)  # Output: "h"

result = find_all_unique_chars_without_extra_space(input_string)
print(result)  # Output: "helo wrd"

