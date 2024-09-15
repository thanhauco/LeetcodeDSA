class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pathSum(root, target_sum):
    all_paths = []  # To store all valid paths

    def dfs(node, current_sum, path):
        if not node:
            return
        
        # Update the current sum and path
        current_sum += node.value
        current_path = path + [node.value]  # Create a new path list

        # Check if it's a leaf node and if the current sum matches the target
        if not node.left and not node.right:
            if current_sum == target_sum:
                all_paths.append(current_path)  # Add the valid path to the list
                return
        
        # Recursively check the left and right subtrees
        dfs(node.left, current_sum, current_path)
        dfs(node.right, current_sum, current_path)

    dfs(root, 0, [])
    return all_paths

# Example usage:
# Constructing a binary tree:
#       5
#      / \
#     4   8
#    /   / \
#   11  5   4
#  /  \      \
# 7    2      1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

target_sum = 18
result = pathSum(root, target_sum)
print(f"Paths that sum to {target_sum}: {result}")