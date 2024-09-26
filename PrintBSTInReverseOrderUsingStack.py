from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_reverse_level_wise(root):
    if root is None:
        return

    stack = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            current_node = queue.popleft()
            level_values.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        stack.append(level_values)

    while stack:
        level_values = stack.pop()
        
        #while (level_values):
        #    print(level_values.pop(), end=" ")
         
        for i in range(1, len(level_values) + 1):
            print(level_values[-i], end=" ") # print reverse

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

# Print the nodes in reverse level-wise order
print_reverse_level_wise(root) # print 5 4 3 2 1 from bottom