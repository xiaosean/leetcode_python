class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs with dp solution
        # create 2D matrix for dp
        # hashmap save visit or not or we can check it is 1 or 0
        # hashmap 0 means can traverse 1 and so on means already traverse
        # make sure without cycle, replace a notation on matrix = -1
        
        n_rows, n_cols = len(matrix), len(matrix[0])
        dp = [[0]*n_cols for _ in range(n_rows)]
        def traverse_4sides(y, x, input_num=-2):
            if y < 0 or y > n_rows-1 or x < 0 or x > n_cols-1 or matrix[y][x] == -1:
                return 0
            if input_num <= matrix[y][x] and input_num >= 0:
                return 0
            if not dp[y][x]:
                num = matrix[y][x]
                matrix[y][x] = -1
                res = [traverse_4sides(y+shift_y, x+shift_x, num) for shift_y, shift_x in [[-1, 0], [1, 0], [0, 1], [0, -1]]]
                matrix[y][x] = num
                dp[y][x] = 1 + max(res)
            return dp[y][x]
        longest = 1               
        for y in range(n_rows):
            for x in range(n_cols):
                longest = max(longest, traverse_4sides(y, x))
        return longest
                
            