class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_str = "".join(row).replace(".", "")
            if len(row_str) > len(set(row_str)):
                return False
        for col_id in range(9):
            row_str = "".join([board[i][col_id] for i in range(9)]).replace(".", "")
            if len(row_str) > len(set(row_str)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block =  [board[i+x_i][j+y_i] for x_i in range(3) for y_i in range(3)] 
                row_str = "".join(block).replace(".", "")
                if len(row_str) > len(set(row_str)):
                    return False
        return True