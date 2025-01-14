class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Base case: Stop DFS if out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            # Mark the current cell as visited by setting it to 0
            grid[r][c] = "0"  # to avoid max recursion depth exceeded error, Ensure we are marking it as a string "0"
            # Explore all 4 directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Found a new island
                    count += 1
                    dfs(r, c)  # Mark the entire island as visited
        
        return count