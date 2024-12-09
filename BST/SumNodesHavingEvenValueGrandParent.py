"""
Problem: Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of the nodes with an even-valued grandparent. A grandparent of a node is the parent of its parent.

Approach:

	1.	Depth First Search (DFS):
	•	Perform a DFS traversal of the tree to explore all nodes.
	2.	Tracking Parent and Grandparent:
	•	While traversing the tree, keep track of the parent and grandparent nodes.
	•	At each node, check if the grandparent’s value is even. If it is, add the current node’s value to the result.
	3.	Post-order Traversal:
	•	Perform a post-order traversal to ensure that we process the children before the current node, so we can pass along the correct parent and grandparent information.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root):
    def dfs(node, parent, grandparent):
        if not node:
            return 0
        
        # If grandparent is even, add the node value to the sum
        sum_val = 0
        if grandparent and grandparent.val % 2 == 0:
            sum_val += node.val
        
        # Traverse the left and right subtree, passing the current node as parent and grandparent
        sum_val += dfs(node.left, node, parent)
        sum_val += dfs(node.right, node, parent)
        
        return sum_val
    
    # Start DFS from the root, with no parent or grandparent
    return dfs(root, None, None)


# Example usage:

"""
        6
       / \
      7   8
     / \    \
    2   7    1
   /
  3
"""
root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(1)
root.left.left.left = TreeNode(3)

print(sumEvenGrandparent(root))  # Output: 10 = (2 + 7 + 1)


"""
        Tree structure:
             6
           /   \
          7     8
         / \   / \
        2   7 1   3
"""
root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)

print(sumEvenGrandparent(root)) # 13 (2 + 7 + 1 + 3)

"""
Deeper tree with mixed grandparent values:
               6
             /   \
            7     8
           / \   / \
          2   9 1   3
         /   
        4    
"""
root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(9)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)

print(sumEvenGrandparent(root)) # 15 ( 2 + 9 + 1 + 3)

