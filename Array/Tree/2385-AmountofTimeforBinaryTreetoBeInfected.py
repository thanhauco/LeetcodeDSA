# this similar to find distance K From Target in a graph
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def amountOfTime(root: TreeNode, start: TreeNode) -> int:
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

    # Step 2: Perform BFS from the start node
    queue = deque([start])
    visited = set([start])
    time = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        time += 1

    # Since we increment time after processing the last level, we return time - 1
    return time - 1

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

start = root.left  # Starting infection from node with value 2

# Calculate the time required for the whole tree to be infected
result = amountOfTime(root, start)
print(result)  # Output: 2