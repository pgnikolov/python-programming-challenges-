def gameOfLife(self, board) -> None:
    rows = len(board)
    cols = len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        for c in range(cols):
            liveCount = 0
            for dr, dc in directions:
                newRow, newCol = r + dr, c + dc
                if valid(newRow, newCol) and board[newRow][newCol] in {1, 2}:
                    liveCount += 1
            if board[r][c] == 1:
                if liveCount < 2 or liveCount > 3:
                    board[r][c] = 2
            else:
                if liveCount == 3:
                    board[r][c] = -1

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == -1:
                board[r][c] = 1
