"""
Given a chemical formula string like "H2O" or "Mg(OH)2", return a dictionary or sorted string representation of each atom and its count. Nested parentheses with multipliers are included, e.g., "K4(ON(SO3)2)2".

Hint 1:

Use a stack to keep track of the current count of atoms as you parse the formula. Push and pop counts when encountering parentheses.

Hint 2:

Process the formula character by character:
	•	If it’s an atom, parse its name and count.
	•	If it’s (, push the current state to the stack.
	•	If it’s ), multiply the atom counts within the parentheses by the multiplier that follows.
"""

import collections

def countOfAtoms(formula):
    def parse():
        count = collections.Counter()
        while i[0] < len(formula):
            char = formula[i[0]]

            if char == '(':
                i[0] += 1  # Move past '('
                inner_count = parse()
                i[0] += 1  # Move past ')'
                
                # Get multiplier
                multiplier = 0
                while i[0] < len(formula) and formula[i[0]].isdigit():
                    multiplier = multiplier * 10 + int(formula[i[0]])
                    i[0] += 1
                
                # Multiply inner count by multiplier
                for atom in inner_count:
                    count[atom] += inner_count[atom] * (multiplier or 1)

            elif char == ')':
                break

            elif char.isupper():
                # Parse element name
                start = i[0]
                i[0] += 1
                while i[0] < len(formula) and formula[i[0]].islower():
                    i[0] += 1
                atom = formula[start:i[0]]

                # Parse count
                multiplier = 0
                while i[0] < len(formula) and formula[i[0]].isdigit():
                    multiplier = multiplier * 10 + int(formula[i[0]])
                    i[0] += 1
                
                count[atom] += multiplier or 1

            else:
                i[0] += 1

        return count

    # Parse the formula
    i = [0]
    result = parse()

    # Format the result
    output = []
    for atom in sorted(result):
        output.append(atom)
        if result[atom] > 1:
            output.append(str(result[atom]))
    return ''.join(output)

# Example usage:
print(countOfAtoms("H2O"))  # Output: "H2O"
print(countOfAtoms("Mg(OH)2"))  # Output: "H2MgO2"
print(countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"