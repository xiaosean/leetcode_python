class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        dp = [0] * n
        # 4 state 
#         0 cooldown can buy
#         1 buy can sell
#         2 buy can cooldown
#         3 cooldown again
        sell = no_book = 0
        buy = has_book = -prices[0]
        for i in range(1, n):
            cur_buy = no_book - prices[i]
            cur_sell = prices[i] + max(buy, has_book)
            cur_has_book = max(buy, has_book)
            cur_no_book = max(sell, no_book)
            
            buy = cur_buy
            sell = cur_sell
            has_book = cur_has_book
            no_book = cur_no_book

            dp[i] = max(sell, no_book)
        # print(dp)
        return max(dp)
            
            
            