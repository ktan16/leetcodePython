from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # hashmap k = row, v = set of numbers in row
        rows = defaultdict(set)
        # hashmap k = col, v = set of numbers in col
        cols = defaultdict(set)
        # hashmap k = (row//3 col//3), v = set of numbers in square
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': # skip dots
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3, c//3)]): # if num exists, return false
                    return False
                
                # add to dictionaries
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        
        return True
    
    def m_isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        SIZE = 9

        # check through each row, add each num to row_list
        # if num already in row_list, return False
        # else append num to row_list
        for row in board:
            row_list = []
            for col in row:
                if col != '.':
                    if col in row_list:
                        return False
                    else:
                        row_list.append(col)

        # check through each col, add each col to col_list
        # if num already in col_list, return False
        # else append num to col_list
        for col in range(SIZE):
            col_list = []
            for row in board:
                if row[col] != '.':
                    if row[col] in col_list:
                        return False
                    else:
                        col_list.append(row[col])

        
        return True

        
ob = Solution()

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(ob.isValidSudoku(board))