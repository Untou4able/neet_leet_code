""" Love sudoku, it was a fun one.
    sets for squares, rows and cols are even faster, but take more space
"""


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_hash = {
            'squares': [[] for _ in range(len(board))],
            'rows': [[] for _ in range(len(board))],
            'cols': [[] for _ in range(len(board))]
        }
        for rowi, row in enumerate(board):
            for coli, col in enumerate(row):
                if not col == '.':
                    if col in sudoku_hash['rows'][rowi]:
                        print(col, 'in row', sudoku_hash['rows'][rowi])
                        return False
                    if col in sudoku_hash['cols'][coli]:
                        print(col, 'in col', sudoku_hash['cols'][coli])
                        return False
                    squarei = (rowi // 3) * 3 + (coli // 3)
                    if col in sudoku_hash['squares'][squarei]:
                        print(col, 'in square', sudoku_hash['squares'][squarei])
                        return False
                    sudoku_hash['cols'][coli].append(col)
                    sudoku_hash['rows'][rowi].append(col)
                    sudoku_hash['squares'][squarei].append(col)
        return True

s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
