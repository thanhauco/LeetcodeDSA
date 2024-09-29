class Solution(object):
    def islandPerimeter(self, grid):
        """
        Calculate the perimeter of a single island in the grid.
        Assumes there is only one island in the grid.
        
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        
        return perimeter

    def multipleIslandsPerimeter(self, grid):
        """
        Calculate the total perimeter of all islands in the grid.
        Works for any number of islands, including a single island.
        
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        land_cells = 0
        adjacent_pairs = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    # Check right neighbor
                    if j < cols - 1 and grid[i][j+1] == 1:
                        adjacent_pairs += 1
                    # Check bottom neighbor
                    if i < rows - 1 and grid[i+1][j] == 1:
                        adjacent_pairs += 1
        
        return 4 * land_cells - 2 * adjacent_pairs

    def countIslands(self, grid):
        """
        Count the number of islands in the grid.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return
            grid[i][j] = -1  # Mark as visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    islands += 1
        
        # Restore the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == -1:
                    grid[i][j] = 1
        
        return islands

# Test the functions
if __name__ == "__main__":
    solution = Solution()

    # Test case for multiple islands (2 islands)
    two_islands_grid = [
        [0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0]
    ]
    
    # Test the countIslands function
    island_count = solution.countIslands(two_islands_grid)
    print(f"Number of islands: {island_count}")

    # Test single island function (will only consider the first island it encounters)
    single_result = solution.islandPerimeter(two_islands_grid)
    print(f"Perimeter of first island encountered: {single_result}")

    # Test multiple islands function
    multiple_result = solution.multipleIslandsPerimeter(two_islands_grid)
    print(f"Total perimeter of all islands: {multiple_result}")
