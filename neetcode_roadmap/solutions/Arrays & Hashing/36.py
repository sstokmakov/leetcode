# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in boxes[(i // 3, j // 3)]:
                        return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[(i // 3, j // 3)].add(board[i][j])
        return True