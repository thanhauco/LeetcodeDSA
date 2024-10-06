class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    # Helper function to construct the BST
    def convert_list_to_bst(left, right):
        if left > right:
            return None
        
        # Choose the middle element as the root
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        # Recursively build the left and right subtrees
        root.left = convert_list_to_bst(left, mid - 1)
        root.right = convert_list_to_bst(mid + 1, right)
        
        return root

    return convert_list_to_bst(0, len(nums) - 1)

# Example Usage:
sorted_array = [-10, -3, 0, 5, 9]
bst_root = sortedArrayToBST(sorted_array)

# Function to print inorder traversal of the BST
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=' ')
        inorder_traversal(node.right)

# Print the inorder traversal of the constructed BST
inorder_traversal(bst_root)  # Output: -10 -3 0 5 9