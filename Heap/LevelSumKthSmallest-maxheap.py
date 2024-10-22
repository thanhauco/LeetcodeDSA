from collections import deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1  # Handle empty tree case
        
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
            
            # Use a max-heap to track the k smallest sums
            heapq.heappush(level_sums, -current_level_sum)  # Push negative to simulate max-heap
            if len(level_sums) > k:
                heapq.heappop(level_sums)  # Remove the largest sum if we exceed size k

        if len(level_sums) < k:
            return -1  # Not enough levels
        
        return -level_sums[0]  # The k-th smallest sum is the largest in the max-heap

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
k = 1
print(solution.kthSmallestLevelSum(root, k))  # Output: Expected k-th smallest level sum