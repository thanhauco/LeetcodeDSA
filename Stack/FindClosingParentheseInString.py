def find_closing_parenthesis(sentence: str, opening_pos: int) -> int:
    # Check if the opening position is valid
    if sentence[opening_pos] != '(':
        return -1  # Return -1 if the position is not an opening parenthesis

    stack = []
    
    # Traverse the string starting from the opening parenthesis position
    for i in range(opening_pos, len(sentence)):
        if sentence[i] == '(':
            stack.append(i)  # Push the index of the opening parenthesis onto the stack
        elif sentence[i] == ')':
            if stack:
                last_opening_pos = stack.pop()  # Pop the last opening parenthesis index
                if last_opening_pos == opening_pos:
                    return i  # Return the index of the corresponding closing parenthesis

    return -1  # Return -1 if no matching closing parenthesis is found

# Example usage
sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
opening_pos = 10  # Position of the first opening parenthesis '('
closing_pos = find_closing_parenthesis(sentence, opening_pos)

print(closing_pos)  # Output: 79