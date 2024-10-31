class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Initialize sets to track numbers in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                # Skip empty cells
                if board[i][j] == '.':
                    continue
                    
                num = board[i][j]
                
                # Calculate which 3x3 box we're in
                box_idx = (i // 3) * 3 + j // 3
                
                # Check if number already exists in row, column, or box
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[box_idx]):
                    return False
                    
                # Add number to respective sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
            
            return True
            