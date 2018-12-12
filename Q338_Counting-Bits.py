class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        dp = [0 for _ in range(num+1)]
        dp[1] = 1
        bin_value = 2
        for i in range(2,num+1):
            if int(i/2) == bin_value:
                bin_value *= 2
            dp[i] = dp[i-bin_value] + 1
        return dp
        