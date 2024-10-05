from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def distanceK(root: TreeNode, target: TreeNode, K: int):
    # Step 1: Build the graph using parent pointers
    graph = defaultdict(list)
    
    def build_graph(node, parent):
        if not node:
            return
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        build_graph(node.left, node)
        build_graph(node.right, node)

    build_graph(root, None)

    # Step 2: Perform BFS from the target node
    queue = deque([target])
    visited = set([target])
    distance = 0

    while queue:
        if distance == K:
            return [node.val for node in queue]  # Return the values at distance K
        distance += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return []

# Example Usage:
# Constructing the binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

target = root.left  # Target is node with value 2
K = 1

# Find all nodes at distance K from target
result = distanceK(root, target, K)
print(result)  # Output: [1, 4, 5]