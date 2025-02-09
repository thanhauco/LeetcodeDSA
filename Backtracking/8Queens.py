def is_safe(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board) and board[x][y] == -1

def solve_knight_tour(n, start_x=0, start_y=0):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def solve_util(x, y, movei):
        if movei == n * n:  # Nếu đã đi qua tất cả các ô
            return True
        for move in moves:
            next_x, next_y = x + move[0], y + move[1]
            if is_safe(next_x, next_y, board):
                board[next_x][next_y] = movei
                print(f"Step {movei}: Move to ({next_x}, {next_y})")  # Hiển thị bước di chuyển
                if solve_util(next_x, next_y, movei + 1):
                    return True
                board[next_x][next_y] = -1  # Quay lui
        return False

    def print_board(board):
        for row in board:
            print(row)
        print()  # Thêm dòng trống giữa các bước

    # Khởi đầu từ ô (start_x, start_y)
    board[start_x][start_y] = 0
    print_board(board)  # Hiển thị bàn cờ ban đầu
    if solve_util(start_x, start_y, 1):
        print("Giải pháp tìm thấy!")
    else:
        print("Không tìm được giải pháp")

solve_knight_tour(8, 0, 0)  # Thử với bàn cờ 8x8