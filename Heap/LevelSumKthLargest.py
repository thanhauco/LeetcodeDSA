from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1  # or handle empty tree case as desired
        
        level_sums = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(current_level_sum)

        # Sort the level sums in descending order and return the k-th largest
        level_sums.sort(reverse=True)

        if k > len(level_sums):
            return -1  # or handle the case where k is out of bounds
        
        return level_sums[k - 1]  # k-th largest is at index k-1

# Example usage:
# Constructing a simple BST
#       5
#      / \
#     3   8
#    / \   \
#   2   4   9

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(9)

solution = Solution()
k = 2
print(solution.kthLargestLevelSum(root, k))  # Output: Expected k-th largest level sum