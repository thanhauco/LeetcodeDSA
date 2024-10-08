class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string using preorder without None."""
        def preorder(node):
            if not node:
                return []
            return [str(node.value)] + preorder(node.left) + preorder(node.right)

        return ','.join(preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        values = data.split(',')
        self.index = 0  # Use an index to track the position in the list

        def build_tree():
            if self.index >= len(values):
                return None
            
            node = TreeNode(int(values[self.index]))
            self.index += 1
            
            # Recursively build left and right subtrees
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()

# Example usage
# Constructing the binary tree
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Create a Codec object
codec = Codec()

# Serialize the binary tree
serialized_tree = codec.serialize(root)
print("Serialized tree (preorder without None):", serialized_tree)

# Deserialize the string back to a binary tree
deserialized_tree = codec.deserialize(serialized_tree)

# Function to print the tree in inorder traversal for checking the result
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

print("Inorder traversal of deserialized tree:")
inorder(deserialized_tree)
print()