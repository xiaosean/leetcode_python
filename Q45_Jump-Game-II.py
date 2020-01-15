class Solution:
    def jump(self, nums: List[int]) -> int:
#         Store the steps in each position
#         if newer_arrvals' step less then current step then replace
#         After we run all position, we can get the minimun
#         Trick: use dp solution to get the minumum steps
        n = len(nums)    
        dp = [i for i in range(n)]
        for idx, num in enumerate(nums):
            for jump_pos in range(idx+num, idx, -1):
                if jump_pos < n: 
                    if dp[idx]+1 < dp[jump_pos]:
                        dp[jump_pos] = dp[idx]+1
                    else:
                        break
        return dp[-1]
        