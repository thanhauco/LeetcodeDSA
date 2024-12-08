from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0  # If the tree is empty, return 0.

    queue = deque([root])  # Initialize a queue with the root node.
    depth = 0  # Start with a depth of 0.

    while queue:
        depth += 1  # Increment depth at the start of each level.
        for _ in range(len(queue)):
            node = queue.popleft()  # Process all nodes in the current level.
            # Add children of the current node to the queue for the next level.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))  # Output: 3