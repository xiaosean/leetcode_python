class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [amount+1]*amount
        
        for i in range(1, amount+1):
            dp[i] = min([dp[i]] + [dp[i-coin]+1 for coin in coins if i-coin >= 0])
        
        if dp[-1] == amount+1:
            return -1
        return dp[-1]