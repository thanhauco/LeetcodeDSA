class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def hasPathSum(root, target_sum):
    path = []  # To store the path

    def dfs(node, current_sum):
        if not node:
            return False
        
        # Add the current node's value to the path and the sum
        path.append(node.value)
        current_sum += node.value
        
        # Check if it's a leaf node and if the current sum matches the target
        if not node.left and not node.right:
            if current_sum == target_sum:
                return True
            else:
                path.pop()  # Backtrack if not the correct path
                return False

        # Recursively check the left and right subtrees
        if (dfs(node.left, current_sum) or dfs(node.right, current_sum)):
            return True
        
        path.pop()  # Backtrack if not the correct path
        return False

    if dfs(root, 0):
        return True, path
    else:
        return False, []

# Example usage:
# Constructing a binary tree:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

target_sum = 22
result, path = hasPathSum(root, target_sum)
print(f"Path Exists: {result}")  # Output: True
if result:
    print(f"Path: {path}")  # Output: The path corresponding to the target sum