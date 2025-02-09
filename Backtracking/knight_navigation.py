def knight_moves(position):
    # Possible moves for a knight in chess
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    x, y = position
    valid_moves = []
    
    for move in moves:
        new_x = x + move[0]
        new_y = y + move[1]
        
        # Check if the new position is within the bounds of the chessboard
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            valid_moves.append((new_x, new_y))
    
    return valid_moves

# Example usage
start_position = (4, 4)  # Starting from the center of the board
print(knight_moves(start_position))