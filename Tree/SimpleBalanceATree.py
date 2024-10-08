class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(node, values):
    """Helper function to perform inorder traversal and collect node values."""
    if not node:
        return
    inorder_traversal(node.left, values)
    values.append(node.value)
    inorder_traversal(node.right, values)

def sorted_array_to_bst(values):
    """Helper function to construct a balanced BST from a sorted list of values."""
    if not values:
        return None
    
    mid = len(values) // 2
    root = TreeNode(values[mid])
    
    # Recursively construct the left and right subtrees
    root.left = sorted_array_to_bst(values[:mid])
    root.right = sorted_array_to_bst(values[mid + 1:])
    
    return root

def balance_tree(root):
    """Balances the binary tree."""
    values = []
    inorder_traversal(root, values)  # Step 1: Collect values
    return sorted_array_to_bst(values)  # Step 2: Construct balanced BST

def print_inorder(node):
    """Helper function to print the inorder traversal of the tree."""
    if node:
        print_inorder(node.left)
        print(node.value, end=' ')
        print_inorder(node.right)

# Constructing a larger unbalanced binary tree
# Example Tree Structure:
#            50
#           /  \
#          30   70
#         / \    \
#        20  40   80
#       /
#      10
#     /
#    5
# This structure is unbalanced.

root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.left.left.left = TreeNode(10)
root.left.left.left.left = TreeNode(5)
root.right.right = TreeNode(80)

print("Inorder traversal of original unbalanced tree:")
print_inorder(root)
print("\n")

# Balance the tree
balanced_root = balance_tree(root)

print("Inorder traversal of balanced tree:")
print_inorder(balanced_root)
print()