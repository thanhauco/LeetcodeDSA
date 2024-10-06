class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursively(self.root, val)

    def _insert_recursively(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursively(node.left, val)
        else:  # val >= node.val
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursively(node.right, val)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)

def construct_bst_from_unsorted_array(arr):
    bst = BST()
    for val in arr:
        bst.insert(val)
    return bst.root

# Example Usage:
unsorted_array = [7, 3, 1, 4, 9, 6]
bst_root = construct_bst_from_unsorted_array(unsorted_array)

# Print the inorder traversal of the constructed BST
bst = BST()
bst.root = bst_root
bst.inorder_traversal(bst.root)  # Output: 1 3 4 6 7 9