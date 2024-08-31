def closedIsland(grid):
    def dfs(x, y):
        # If out of bounds or at a water cell, return immediately
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1:
            return
        # Mark the cell as visited
        grid[x][y] = 1
        # Explore all 4 directions
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    # First, mark all land cells connected to the boundary as water
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        if grid[i][0] == 0:
            dfs(i, 0)
        if grid[i][cols - 1] == 0:
            dfs(i, cols - 1)
    
    for j in range(cols):
        if grid[0][j] == 0:
            dfs(0, j)
        if grid[rows - 1][j] == 0:
            dfs(rows - 1, j)
    
    # Now, count all closed islands
    closed_islands_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                dfs(i, j)
                closed_islands_count += 1
    
    return closed_islands_count

# Test case
grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]

print("Input grid:")
for row in grid:
    print(row)

result = closedIsland(grid)
print(f"\nNumber of closed islands: {result}")
