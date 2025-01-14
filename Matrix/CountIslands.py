from collections import deque

def numIslandsDFS(grid):
    if not grid:
        return 0
    
    def dfs(i, j):
        # If the current cell is out of bounds or is water, stop the exploration
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return
        
        # Mark the cell as visited by setting it to 0
        grid[i][j] = 0 # to avoid max recursion depth error
        
        # Explore all four directions
        dfs(i-1, j)  # Up
        dfs(i+1, j)  # Down
        dfs(i, j-1)  # Left
        dfs(i, j+1)  # Right
    
    island_count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Found an unvisited part of an island
                dfs(i, j)  # Perform DFS to mark the entire island
                island_count += 1  # Increment the island count
    
    return island_count

def numIslandsBFS(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    island_count = 0
    
    def bfs(i, j):
        queue = deque([(i, j)])
        grid[i][j] = 0  # Mark as visited
        
        while queue:
            curr_i, curr_j = queue.popleft()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
            
            for di, dj in directions:
                next_i, next_j = curr_i + di, curr_j + dj
                if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == 1:
                    queue.append((next_i, next_j))
                    grid[next_i][next_j] = 0  # Mark as visited
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                bfs(i, j)
                island_count += 1
    
    return island_count

# Test cases
if __name__ == "__main__":
    # Test case 1: Multiple islands
    grid1 = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]
    ]
    print("Test case 1:")
    print("Grid:")
    for row in grid1:
        print(row)
    print("Number of islands (DFS):", numIslandsDFS([row[:] for row in grid1]))
    print("Number of islands (BFS):", numIslandsBFS([row[:] for row in grid1]))
    print()

    # Test case 2: Single island
    grid2 = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]
    ]
    print("Test case 2:")
    print("Grid:")
    for row in grid2:
        print(row)
    print("Number of islands (DFS):", numIslandsDFS([row[:] for row in grid2]))
    print("Number of islands (BFS):", numIslandsBFS([row[:] for row in grid2]))
    print()

    # Test case 3: No islands
    grid3 = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    print("Test case 3:")
    print("Grid:")
    for row in grid3:
        print(row)
    print("Number of islands (DFS):", numIslandsDFS([row[:] for row in grid3]))
    print("Number of islands (BFS):", numIslandsBFS([row[:] for row in grid3]))
