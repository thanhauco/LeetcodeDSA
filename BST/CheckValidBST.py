class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def validate(node, low, high):
        if not node:
            return True  # An empty tree is a valid BST
        if not (low < node.val < high):
            return False  # Current node violates the range rule
        # Recursively validate left and right subtrees
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float('-inf'), float('inf'))

# Example usage:
# Construct a valid BST
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(isValidBST(root))  # Output: True

# Construct an invalid BST
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
print(isValidBST(root2))  # Output: False