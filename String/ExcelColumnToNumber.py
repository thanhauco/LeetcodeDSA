def title_to_number(column_title):
    column_number = 0
    for char in column_title:
        # Convert character to number and accumulate
        column_number = column_number * 26 + (ord(char) - ord('A') + 1)
    return column_number

# Example usage:
print(title_to_number("A"))   # Output: 1
print(title_to_number("AB"))  # Output: 28
print(title_to_number("ZY"))  # Output: 701