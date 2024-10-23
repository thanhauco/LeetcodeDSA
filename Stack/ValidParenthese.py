def is_valid_parentheses(s: str) -> bool:
    stack = []

    for char in s:
        if char in '({[':  # If it's an opening bracket
            stack.append(char)
        elif char in ')}]':  # If it's a closing bracket
            if not stack:
                return False  # Stack is empty, no opening bracket for this closing bracket
            top = stack.pop()
            # Check if the popped opening bracket matches the closing one
            if (char == ')' and top != '(') or \
               (char == '}' and top != '{') or \
               (char == ']' and top != '['):
                return False

    return not stack  # If stack is empty, all brackets are valid

def is_valid_parentheses_2(s: str) -> bool:
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys():  # If it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False  # Stack is empty or top does not match
            stack.pop()  # Pop the matching opening bracket

    return not stack  # If stack is empty, all brackets are valid



# Example usage
print(is_valid_parentheses_2("()[]{}"))  # Output: True
print(is_valid_parentheses_2("(]"))      # Output: False
print(is_valid_parentheses_2("([{}])"))   # Output: True