from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bottom_view(root):
    if not root:
        return []

    bottom_view_map = {}  # Dictionary to store the bottom view nodes
    queue = deque([(root, 0)])  # (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()

        # Update the bottom view map with the current node
        bottom_view_map[hd] = node.value

        # Add left and right children to the queue with updated horizontal distances
        if node.left:
            queue.append((node.left, hd - 1))  # Move left decreases HD
        if node.right:
            queue.append((node.right, hd + 1))  # Move right increases HD

    # Extract the bottom view from the map sorted by horizontal distance
    bottom_view_list = [bottom_view_map[hd] for hd in sorted(bottom_view_map.keys())]
    return bottom_view_list

# Example usage
# Constructing the binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
#    /       / \
#   7       8   9

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

# Get the bottom view of the binary tree
bottom_view_result = bottom_view(root)

# Output the result
print("The bottom view of the binary tree is:", bottom_view_result)