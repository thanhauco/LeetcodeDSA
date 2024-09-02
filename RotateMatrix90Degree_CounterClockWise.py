def rotate_matrix_90_counterclockwise(matrix):
    N = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each column to achieve a 90-degree counterclockwise rotation
    for j in range(N):
        for i in range(N // 2):
            matrix[i][j], matrix[N - 1 - i][j] = matrix[N - 1 - i][j], matrix[i][j]
    
    return matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(rotate_matrix_90_counterclockwise(matrix))