from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode) :
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            if i == level_length - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

def leftSideView(root: TreeNode) :
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            if i == 0:  # Change to capture the first node of each level
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Add test data for the rightSideView function
if __name__ == "__main__":
    # Create a larger sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    # Test the rightSideView function
    print("right side: " + str(rightSideView(root)))  # Expected output: [1, 3, 6, 8]
    print("left side: " + str(leftSideView(root)))  # Expected output: [1, 2, 4]
