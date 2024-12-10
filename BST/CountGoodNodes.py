# count good nodes in a binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countGoodNodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        good_nodes = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        good_nodes += dfs(node.left, max_val)
        good_nodes += dfs(node.right, max_val)
        return good_nodes
    return dfs(root, float('-inf'))

    

# Example usage:
# Construct a binary tree
#       3
#      / \
#     1   4
#      \   \
#       3   5
root = TreeNode(3, TreeNode(1, None, TreeNode(3)), TreeNode(4, None, TreeNode(5)))
print(countGoodNodes(root))  

