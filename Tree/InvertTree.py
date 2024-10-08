class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def invert_tree(node):
    # Base case: if the node is None, return None
    if not node:
        return None

    # Swap the left and right children
    node.left, node.right = node.right, node.left

    # Recursively invert the left and right subtrees
    invert_tree(node.left)
    invert_tree(node.right)

    return node

# Function to print the tree in inorder traversal for checking the result
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

# Example usage
# Constructing the binary tree
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Original tree (inorder):")
inorder(root)
print()

# Invert the binary tree
invert_tree(root)

print("Inverted tree (inorder):")
inorder(root)
print()