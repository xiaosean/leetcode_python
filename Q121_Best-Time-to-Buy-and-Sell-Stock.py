class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = temp_profit = 0
        incresing = [tomorrow-today for today, tomorrow in zip(prices[:-1],prices[1:])]
    #     print(incresing)
        for price in incresing:
            temp_profit += price
            if temp_profit < 0:
                temp_profit = 0
            else:
                max_profit = max(max_profit, temp_profit)
        return max_profit