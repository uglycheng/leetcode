class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [[True for k in range(9)] for k in range(9)]
        column = [[True for k in range(9)] for k in range(9)]
        block = [[True for k in range(9)] for k in range(9)]
        tracing_record = [[0 for k in range(9)] for k in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    value = int(board[i][j]) - 1
                    row[i][value] = False
                    column[j][value] = False
                    block[i/3*3 + j/3][value] = False
                    tracing_record[i][j] = 10
        i, j = 0, 0
        while (i!=9 or j!=0) :
            value = tracing_record[i][j]
            back_tracing_or_not = True
            for value in range(tracing_record[i][j], 9):
                if row[i][value] and column[j][value] and block[i/3*3 + j/3][value]:
                    board[i][j] = str(value+1)
                    tracing_record[i][j] = value + 1 
                    row[i][value] = False
                    column[j][value] = False
                    block[i/3*3 + j/3][value] = False
                    i += (j+1) / 9
                    j = (j+1) % 9
                    back_tracing_or_not = False
                    break
            if (value == 8 and back_tracing_or_not) :
                tracing_record[i][j] = 0
                i +=  (j-1) / 9
                j = (j-1) % 9
                while tracing_record[i][j] == 10:
                    i +=  (j-1) / 9
                    j = (j-1) % 9
                num = int(board[i][j]) - 1
                row[i][num] = True
                column[j][num] = True
                block[i/3*3 + j/3][num] = True
            elif i<9 and tracing_record[i][j] == 9:
                num = int(board[i][j]) - 1
                board[i][j] = "."
                tracing_record[i][j] = 0
                row[i][num] = True
                column[j][num] = True
                block[i/3*3 + j/3][num] = True
                i +=  (j-1) / 9
                j = (j-1) % 9
                while tracing_record[i][j] == 10:
                    i +=  (j-1) / 9
                    j = (j-1) % 9
                num = int(board[i][j]) - 1
                row[i][num] = True
                column[j][num] = True
                block[i/3*3 + j/3][num] = True
            elif value == 10:
                i += (j+1) / 9
                j = (j+1) % 9
        return board
                
                
solution = Solution()
board = solution.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])
def isValidSudoku(board):
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
print(isValidSudoku(board))
            



