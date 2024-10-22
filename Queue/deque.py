from collections import deque

# Create a new deque
d = deque([1, 2, 3, 4, 5])

# 1. append(x) - Add x to the right side
d.append(6)  # d is now [1, 2, 3, 4, 5, 6]

# 2. appendleft(x) - Add x to the left side
d.appendleft(0)  # d is now [0, 1, 2, 3, 4, 5, 6]

# 3. pop() - Remove and return an element from the right side
right = d.pop()  # right = 6, d is now [0, 1, 2, 3, 4, 5]

# 4. popleft() - Remove and return an element from the left side
left = d.popleft()  # left = 0, d is now [1, 2, 3, 4, 5]

# 5. extend(iterable) - Extend the right side with elements from the iterable
d.extend([6, 7, 8])  # d is now [1, 2, 3, 4, 5, 6, 7, 8]

# 6. extendleft(iterable) - Extend the left side with elements from the iterable
# Note: The elements are added in reverse order
d.extendleft([0, -1, -2])  # d is now [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

# 7. rotate(n) - Rotate the deque n steps to the right (or left if n is negative)
d.rotate(2)  # d is now [7, 8, -2, -1, 0, 1, 2, 3, 4, 5, 6]
d.rotate(-2)  # d is back to [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

# 8. count(x) - Count the number of deque elements equal to x
count = d.count(1)  # count = 1

# 9. index(x[, start[, stop]]) - Return the position of x in the deque (starting from 'start' and ending at 'stop')
index = d.index(5)  # index = 7

# 10. insert(i, x) - Insert x into the deque at position i
d.insert(5, 'a')  # d is now [-2, -1, 0, 1, 2, 'a', 3, 4, 5, 6, 7, 8]

# 11. remove(value) - Remove the first occurrence of value
d.remove('a')  # d is back to [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

# 12. reverse() - Reverse the elements of the deque in-place
d.reverse()  # d is now [8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]

# 13. maxlen - Get the maximum size of the deque (if it's size-limited)
d = deque([1, 2, 3], maxlen=3)
print(d.maxlen)  # Output: 3

# 14. clear() - Remove all elements from the deque
d.clear()  # d is now an empty deque

# 15. copy() - Create a shallow copy of the deque
d = deque([1, 2, 3])
d_copy = d.copy()