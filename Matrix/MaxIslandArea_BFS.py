from collections import deque

def max_island_area(grid):
    if not grid:
        return 0

    max_area = 0
    rows, cols = len(grid), len(grid[0])

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = 0  # Mark as visited
        area = 0

        while queue:
            x, y = queue.popleft()
            area += 1  # Count the current land cell

            # Explore all 4 directions (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 0  # Mark as visited
                    queue.append((new_x, new_y))

        return area

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found an unvisited land cell
                island_area = bfs(i, j)
                max_area = max(max_area, island_area)

    return max_area

# Example usage:
grid = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1]
]

print(max_island_area(grid))  # Output: 4