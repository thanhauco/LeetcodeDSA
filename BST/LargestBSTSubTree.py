class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Solution Approach:

	1.	Definition of BST: A Binary Search Tree is a tree where, for every node:
	•	The left subtree contains only nodes with values less than the node’s value.
	•	The right subtree contains only nodes with values greater than the node’s value.
	2.	DFS Traversal:
	•	We need to perform a DFS traversal, and at each node, determine if the subtree rooted at that node is a valid BST.
	•	If a subtree is a BST, calculate its size. Track the largest BST subtree found so far.
	3.	Tracking Information:
	•	For each node, we need to track:
	•	Whether the subtree rooted at the node is a BST.
	•	The size of the BST.
	•	The minimum and maximum values in the subtree (to ensure the BST property holds).
"""
def largestBSTSubtree(root):
    def dfs(node):
        if not node:
            return (True, 0, float('inf'), float('-inf'))  # (isBST, size, min_val, max_val)
        
        # Recursively check the left and right subtrees
        left_is_bst, left_size, left_min, left_max = dfs(node.left)
        right_is_bst, right_size, right_min, right_max = dfs(node.right)
        
        # Check if the current node forms a valid BST
        if left_is_bst and right_is_bst and node.val > left_max and node.val < right_min:
            # It's a valid BST
            size = left_size + right_size + 1
            min_val = min(node.val, left_min)
            max_val = max(node.val, right_max)
            return (True, size, min_val, max_val)
        else:
            # Not a valid BST, return size of the largest valid BST in the left or right subtree
            size = max(left_size, right_size)
            return (False, size, 0, 0)
    
    # Start DFS from the root
    _, largest_bst_size, _, _ = dfs(root)
    return largest_bst_size

# Example usage:
# This function finds the size of the largest BST subtree in a given binary tree.
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(20)

print(largestBSTSubtree(root))  # Output: 3 (The largest BST is the subtree with root value 5)