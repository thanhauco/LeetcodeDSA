# use extra space
def rotate_matrix_180(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    
    # Create a new matrix with the same dimensions
    rotated = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            # Rotate each element 180 degrees
            rotated[rows - 1 - i][cols - 1 - j] = matrix[i][j]
    
    return rotated

# don't use extra space
def rotate_matrix_180_in_place(matrix):
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(rows // 2):
        for j in range(cols):
            # Swap elements
            matrix[i][j], matrix[rows - 1 - i][cols - 1 - j] = matrix[rows - 1 - i][cols - 1 - j], matrix[i][j]
    
    # If the number of rows is odd, handle the middle row
    if rows % 2 == 1:
        mid = rows // 2
        for j in range(cols // 2):
            matrix[mid][j], matrix[mid][cols - 1 - j] = matrix[mid][cols - 1 - j], matrix[mid][j]

# Example usage with a 5x5 matrix
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print("Original matrix:")
for row in matrix:
    print(row)

rotated_matrix = rotate_matrix_180(matrix)

print("\nRotated matrix (180 degrees):")
for row in rotated_matrix:
    print(row)

rotate_matrix_180_in_place(matrix)

print("\nRotated matrix (180 degrees, in-place):")
for row in matrix:
    print(row)