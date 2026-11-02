from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in rows[r]:
                    return False
                
                rows[r].add(num)

                if num in cols[c]:
                    return False
                
                cols[c].add(num)

                if num in squares[r // 3, c // 3]:
                    return False

                squares[r//3, c//3].add(num)
        return True