def rotate_matrix_in_place(matrix):
    N = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(N):
        matrix[i].reverse()
    
    return matrix

# give me 4x4 matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(rotate_matrix_in_place(matrix))