class Node:
    def __init__(self, value=0, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return

    queue = [root]  # Initialize the queue with the root node

    while queue:
        level_size = len(queue)  # Number of nodes at the current level

        for i in range(level_size):
            node = queue.pop(0)  # Get the front node from the queue

            # Connect to the next node in the queue if it exists
            if i < level_size - 1:  # Not the last node in the level
                node.next = queue[0]

            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # After processing the current level, connect the last node of this level to the first node of the next level
        if queue:
            node.next = queue[0]  # Last node points to the first node of the next level

# Example usage
# Constructing a perfect binary tree
#         100
#        / \
#       20  50
#      / \   \
#     25  75  300
#.              \
#               400

root = Node(100)
root.left = Node(20)
root.right = Node(50)
root.left.left = Node(25)
root.left.right = Node(75)
root.right.right = Node(300)
root.right.right.right = Node(400)


connect(root)

# Function to print the next pointers
def print_next_pointers(node):
    while node:
        print(f'Node {node.value} next ->', end=' ')
        if node.next:
            print(node.next.value)
        else:
            print('None')
        node = node.next

# Print next pointers for the first level
print("Next pointers for :")
print_next_pointers(root)
