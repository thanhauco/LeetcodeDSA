from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTreeFromLevelOrder(arr):
    if not arr:
        return None  # Return None if the array is empty.
    
    # Create the root node.
    root = TreeNode(arr[0])
    queue = deque([root])  # Queue to assign children to nodes.
    i = 1  # Index for traversing the array.
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        # Assign the left child if not None.
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        # Assign the right child if not None.
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root

# Helper function to print the tree in level-order (for verification).
def printLevelOrder(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones for a cleaner representation.
    while result and result[-1] is None:
        result.pop()
    return result

# Example usage:
arr = [3, 9, 20, None, None, 15, 7]
root = createTreeFromLevelOrder(arr)
print(printLevelOrder(root))  # Output: [3, 9, 20, None, None, 15, 7]