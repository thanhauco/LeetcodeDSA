"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

def exist(board, word):
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])
    visited = [[0] * cols for _ in range(rows)]  # Using 0 for unvisited and 1 for visited

    def print_visited():
        for row in visited:
            print(row)
        print()  # Newline for better readability

    def dfs(r, c, index):
        # Base case: if we have matched all characters
        if index == len(word):
            return True
        # Check boundaries and if the cell has already been visited
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] == 1 or board[r][c] != word[index]:
            return False
        
        # Mark the cell as visited
        visited[r][c] = 1
        print_visited()  # Print visited matrix after marking
        
        # Explore all four directions: up, down, left, right
        found = (dfs(r + 1, c, index + 1) or 
                 dfs(r - 1, c, index + 1) or 
                 dfs(r, c + 1, index + 1) or 
                 dfs(r, c - 1, index + 1))
        
        # Backtrack: unmark the cell
        visited[r][c] = 0
        print_visited()  # Print visited matrix after backtracking
        
        return found

    # Start DFS from each cell in the board
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False

# Example usage
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print("Searching for 'ABCCED':", exist(board, "ABCCED"))  # Output: True
print("Searching for 'SEE':", exist(board, "SEE"))          # Output: True
print("Searching for 'ABCB':", exist(board, "ABCB"))        # Output: False