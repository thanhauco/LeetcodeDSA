def max_island_area(grid):
    if not grid:
        return 0

    max_area = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        # Mark the cell as visited
        grid[r][c] = 0
        area = 1  # Count the current land cell

        # Explore all 4 directions (up, down, left, right)
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)

        return area

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found an unvisited land cell
                island_area = dfs(i, j)
                max_area = max(max_area, island_area)

    return max_area

# Example usage:
grid = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
    [1, 1, 0, 1, 1]
]

print(max_island_area(grid))  # Output: 4