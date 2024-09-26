from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_level_wise(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# Create a bigger binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(6)
root.left.right = Node(7)
root.right.left = Node(4)
root.right.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)

# Print the nodes level-wise
print_level_wise(root)