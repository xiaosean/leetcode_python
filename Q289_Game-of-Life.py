class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_neighbors_cnt(i, j):
            neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], 
                         [0, 1], [1, -1], [1, 0], [1, 1]]
            cnt = 0
            for y, x in neighbors:
                next_y = i+y
                next_x = j+x
                if 0 <= next_y < len(board) and 0 <= next_x < len(board[0]):
                    cnt += board[next_y][next_x]%10
            if board[i][j] == 1 and (cnt == 2 or cnt == 3):
                board[i][j] += 10
            elif board[i][j] == 0 and cnt == 3:
                board[i][j] += 10

        for i in range(len(board)):
            for j in range(len(board[0])):
                get_neighbors_cnt(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] //= 10
        