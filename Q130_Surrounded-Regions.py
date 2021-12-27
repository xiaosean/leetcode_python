class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs solution 
        def dfs(y, x, res=[]):
            if y < 0 or y >= n or x < 0 or x >= m or board[y][x] == 'X' or board[y][x] == '-':
                return False
            # if ===== board[y][x] == 'O' =====
            board[y][x] = "-"
            res += [(y, x)]
            dfs(y-1, x)
            dfs(y+1, x)
            dfs(y, x-1)
            dfs(y, x+1)
            return True

        n, m  = len(board), len(board[0])
        res = []
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)
        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n-1][j] == 'O':
                dfs(n-1, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'