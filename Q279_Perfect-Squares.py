class Solution:
    def numSquares(self, n: int) -> int:
        power_dict = {1:1}
        for i in range(1, n+1):
            i_power = i**2
            if i_power > n:
                break
            power_dict[i] = i_power
        keys = power_dict.keys()
        dp = [0]
        cur_idx = 1
        for i in range(1, n+1):
            if cur_idx in power_dict and i == power_dict[cur_idx]:
                dp += [1]
                cur_idx += 1
            else:
                dp += [min((dp[i-power_dict[j]] + 1 for j in range(1, cur_idx)))]
            
        return dp[n]