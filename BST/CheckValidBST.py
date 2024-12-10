class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
    if not root:
        return True
    
    # Check the current node's value against the valid range
    if not (min_val < root.val < max_val):
        return False
    
    # Recursively check left and right subtrees
    return (isValidBST(root.left, min_val, root.val) and
            isValidBST(root.right, root.val, max_val))

# Example Usage:
# Constructing a valid BST
#        2
#       / \
#      1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isValidBST(root))  # Output: True


# Construct an invalid BST
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
print(isValidBST(root2))  # Output: False

