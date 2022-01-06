class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n_cols = len(word1)
        n_rows = len(word2)
        dp = [[0] * n_cols for _ in range(n_rows)]
        for col_idx, letter1 in enumerate(word1):
            for row_idx, letter2 in enumerate(word2):
                if letter1 == letter2:
                    if col_idx and row_idx:
                        dp[row_idx][col_idx] = 1 + dp[row_idx-1][col_idx-1]
                    else:
                        dp[row_idx][col_idx] = 1
                else:
                    dp[row_idx][col_idx] = max(dp[row_idx-1][col_idx], dp[row_idx][col_idx-1])
        print(dp)
        return n_cols+n_rows - 2*dp[-1][-1]
              
        
#     ~~~
#       | s | e | a
#     e | 0 | 1 | 1
#     a | 0 | 1 | 2
#     t | 0 | 1 | 2
#     ~~~
    
    
#     ~~~
#       | l | e | e | t | c | o | d | e
#     e | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1
#     t | 0 | 1 | 1 | 2 | 2 | 2 |  
#     c | 0 | 1 | 1 | 2 | 3 | 3
#     o | 0 | 1 | 1 | 2 | 3 | 4 
#     ~~~