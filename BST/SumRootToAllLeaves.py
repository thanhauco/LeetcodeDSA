class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_root_to_leaf(root):
    def dfs(node, current_sum):
        if not node:
            return 0
        current_sum = current_sum * 10 + node.value
        if not node.left and not node.right:  # Leaf node
            return current_sum
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)

    return dfs(root, 0)

# Create a sample binary tree
# Example tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Call the function and print the result
result = sum_root_to_leaf(root)
print(result)  # Output: 262 (from paths 124 and 125, and 13)
