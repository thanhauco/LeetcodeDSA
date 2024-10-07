class Node:
    def __init__(self, value=0, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

def connect_leaves(root):
    if not root:
        return None

    leaves = []
    
    # Helper function to perform DFS and collect leaf nodes
    def dfs(node):
        if not node:
            return
        # If it's a leaf node, add to leaves list
        if not node.left and not node.right:
            leaves.append(node)
        else:
            dfs(node.left)
            dfs(node.right)

    # Perform DFS to collect leaves
    dfs(root)
    
    # Connect the leaf nodes
    for i in range(len(leaves) - 1):
        leaves[i].next = leaves[i + 1]
    if leaves:
        leaves[-1].next = None  # Last leaf points to None

    return leaves[0] if leaves else None  # Return the head of the leaf linked list

# Example usage
# Constructing the binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Connect leaves
connect_leaves(root)

# Function to print the next pointers of leaf nodes
def print_leaf_next_pointers(node):
    while node:
        print(f'Leaf Node {node.value} next ->', end=' ')
        if node.next:
            print(node.next.value)
        else:
            print('None')
        node = node.next

# Print the next pointers for the leaf nodes
print("Next pointers for leaf nodes:")
print_leaf_next_pointers(root.left.left)  # Starting from leaf node 4