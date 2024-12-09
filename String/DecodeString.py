def decodeString(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)  # Build the multiplier
        elif char == "[":
            stack.append((current_string, current_number))
            current_string, current_number = "", 0  # Reset for the new bracketed substring
        elif char == "]":
            prev_string, repeat_count = stack.pop()
            current_string = prev_string + current_string * repeat_count
        else:
            current_string += char  # Build the current string

    return current_string

# Example usage:
print(decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(decodeString("3[a2[c]]"))   # Output: "accaccacc"
print(decodeString("4[d3[a2[c]]]")) # Output: "daccaccaccdaccaccaccdaccaccaccdaccaccacc"