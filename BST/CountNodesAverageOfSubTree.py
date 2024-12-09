class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This function counts the number of nodes in a binary tree where the value of each node is equal to the average of the values in its subtree.
def averageOfSubtree(root):
    def dfs(node):
        if not node:
            return (0, 0, 0)  # (sum, count, num_good_nodes)
        
        # Recursively compute for left and right subtrees
        left_sum, left_count, left_good = dfs(node.left)
        right_sum, right_count, right_good = dfs(node.right)
        
        # Subtree sum and count including the current node
        subtree_sum = left_sum + right_sum + node.val
        subtree_count = left_count + right_count + 1
        
        # Check if the node's value matches the average of the subtree
        average = subtree_sum // subtree_count
        is_good = 1 if node.val == average else 0
        
        # Total "good" nodes in this subtree
        total_good = left_good + right_good + is_good
        
        return (subtree_sum, subtree_count, total_good)
    
    # Start DFS and return the total count of good nodes
    return dfs(root)[2]

# Example usage:
root = TreeNode(4)
root.left = TreeNode(8)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.right = TreeNode(6)

print(averageOfSubtree(root))  # Output: 5