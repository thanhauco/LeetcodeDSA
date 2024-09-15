class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def hasPathSum(root, target_sum):
    def dfs(node, current_sum, path):
        if not node:
            return False, []

        # Update the current sum and path
        current_sum += node.value
        current_path = path + [node.value]  # Create a new path list

        # Check if it's a leaf node and if the current sum matches the target
        if not node.left and not node.right:
            if current_sum == target_sum:
                return True, current_path  # Return the current path
            else:
                return False, []

        # Recursively check the left and right subtrees
        left_result, left_path = dfs(node.left, current_sum, current_path)
        if left_result:
            return True, left_path

        right_result, right_path = dfs(node.right, current_sum, current_path)
        if right_result:
            return True, right_path

        return False, []

    result, path = dfs(root, 0, [])
    return result, path if result else []

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