class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0  # Base case: If the tree is empty, the depth is 0.
    
    # Using Post Order Traversal
    # Recursively find the depth of left and right subtrees.
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # The depth of the tree is the maximum of the two depths + 1 (for the current node).
    return 1 + max(left_depth, right_depth)

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))  # Output: 3





