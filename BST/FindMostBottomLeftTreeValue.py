# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # If the tree is empty, return None
        if not root:
            return None
        
        # Use level-order traversal (BFS)
        queue = [root]
        leftmost_value = root.val
        
        # Continue until the queue is empty
        while queue:
            # Store the number of nodes at current level
            level_size = len(queue)
            
            # Iterate through current level
            for i in range(level_size):
                # Get and remove the first node in the queue
                node = queue.pop(0)
                
                # For the first node in each level (leftmost),
                # update the leftmost_value
                if i == 0:
                    leftmost_value = node.val
                
                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost_value

import unittest

# Assuming the previous TreeNode and Solution classes are defined

class TestBottomLeftTreeValue(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_single_node_tree(self):
        """Test a tree with only a root node"""
        root = TreeNode(1)
        self.assertEqual(self.solution.findBottomLeftValue(root), 1)
    
    def test_balanced_tree(self):
        """Test a balanced tree"""
        #       1
        #     /   \
        #    2     3
        #   / \   / \
        #  4   5 6   7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.findBottomLeftValue(root), 4)
    
    def test_unbalanced_left_heavy_tree(self):
        """Test a tree that is heavily skewed to the left"""
        #        1
        #       /
        #      2
        #     /
        #    3
        #   /
        #  4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.findBottomLeftValue(root), 4)
    
    def test_unbalanced_right_heavy_tree(self):
        """Test a tree with the bottom-left value not on the leftmost branch"""
        #        1
        #         \
        #          2
        #         / \
        #        3   4
        #           /
        #          5
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        self.assertEqual(self.solution.findBottomLeftValue(root), 5)
    
    def test_empty_tree(self):
        """Test an empty tree"""
        root = None
        self.assertIsNone(self.solution.findBottomLeftValue(root))
    
    def test_two_level_tree(self):
        """Test a two-level tree"""
        #     1
        #    / \
        #   2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.findBottomLeftValue(root), 2)
    
    def test_complex_tree(self):
        """Test a more complex tree structure"""
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        #   /         /
        #  8         9
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.right.right.left = TreeNode(9)
        self.assertEqual(self.solution.findBottomLeftValue(root), 8)

if __name__ == '__main__':
    unittest.main()