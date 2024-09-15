class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')  # Initialize to the smallest possible value
    max_path = []  # To store the path corresponding to the maximum sum

    def dfs(node):
        nonlocal max_sum, max_path
        if not node:
            return 0, []  # Return sum and empty path
        
        # Compute the maximum path sum from left and right children
        left_sum, left_path = dfs(node.left)
        right_sum, right_path = dfs(node.right)

        # Consider only positive contributions
        left_sum = max(left_sum, 0)
        right_sum = max(right_sum, 0)

        # Calculate the current path sum
        current_sum = node.value + left_sum + right_sum
        
        # Update the global maximum path sum and path
        if current_sum > max_sum:
            max_sum = current_sum
            max_path = left_path + [node.value] + right_path  # Update the path
        
        # Return the maximum sum and the path that leads to it
        if left_sum > right_sum:
            return node.value + left_sum, left_path + [node.value]
        else:
            return node.value + right_sum, right_path + [node.value]

    dfs(root)
    return max_sum, max_path


# Example usage:
# Constructing a binary tree:
#       -10
#       /  \
#      9   20
#          /  \
#         15   7

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result, path = maxPathSum(root)
print(f"Maximum Path Sum: {result}")  # Output: Maximum path sum
print(f"Path: {path}")  # Output: The path corresponding to the maximum path sumß


# Constructing a more complex binary tree:
#       -10
#       /  \
#      9   20
#         /  \
#        15   7
#       / \
#      5   2
#           \
#            1

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(5)
root.right.left.right = TreeNode(2)
root.right.left.right.right = TreeNode(1)

result, path = maxPathSum(root)
print(f"Maximum Path Sum: {result}")  # Output: Maximum path sum
print(f"Path: {path}")  # Output: The path corresponding to the maximum path sum