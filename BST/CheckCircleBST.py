class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def detect_cycle(root):
    visited = set()
    
    def dfs(node):
        if not node:
            return False
        if node in visited:
            return True  # Cycle detected
        visited.add(node)
        return dfs(node.left) or dfs(node.right)
    
    return dfs(root)

# Example Usage
# Construct a binary tree with a cycle:
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
node3.left = node2  # Creating a cycle here

print(detect_cycle(node1))  # Output: True