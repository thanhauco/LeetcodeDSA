from collections import deque

def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()

    # Initialize the queue with all '0' cells
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                queue.append((r, c))
                dist[r][c] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Perform BFS
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist

# Test the function
mat1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print("Input matrix 1:")
for row in mat1:
    print(row)
result1 = updateMatrix(mat1)
print("Output matrix 1:")
for row in result1:
    print(row)
print()

# Test case 2
mat2 = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]
print("Input matrix 2:")
for row in mat2:
    print(row)
result2 = updateMatrix(mat2)
print("Output matrix 2:")
for row in result2:
    print(row)
