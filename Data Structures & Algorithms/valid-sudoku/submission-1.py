class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            hori_check = set()
            vert_check = set()
            box_check = set()
            for j in range(9):
                if board[i][j] in hori_check:
                    return False
                if board[i][j] != ".":
                    hori_check.add(board[i][j])

                if board[j][i] in vert_check:
                    return False
                if board[j][i] != ".":
                    vert_check.add(board[j][i])

                i2 = ((i//3)*3) + (j//3)
                j2 = ((i%3)*3) + (j%3) 
                if board[i2][j2] in box_check:
                    return False
                if board[i2][j2] != ".":
                    box_check.add(board[i2][j2])
            
        return True