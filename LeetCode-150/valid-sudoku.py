class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != '.':
                    if cell in rows[i]:
                        return False
                    if cell in cols[j]:
                        return False
                    box_index = (i // 3) * 3 + (j // 3)
                    if cell in boxes[box_index]:
                        return False

                    rows[i].add(cell)
                    cols[j].add(cell)
                    boxes[box_index].add(cell)

        return True
