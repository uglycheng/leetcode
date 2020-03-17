class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[False for k in range(9)] for k in range(9)]
        column = [[False for k in range(9)] for k in range(9)]
        block = [[False for k in range(9)] for k in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    value = int(board[i][j]) - 1
                    block_index = i/3*3 + j/3
                    if row[i][value] or column[j][value] or block[block_index][value]:
                        return False
                    else:
                        row[i][value] = True
                        column[j][value] = True
                        block[block_index][value] = True
        return True
