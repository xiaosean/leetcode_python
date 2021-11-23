class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

    # bottom up and dp can solve this problem
    #         # for num in 1 ... amount
    #         #   we calculate how many ways can change the num to the coin list.
        dp = [1] + [0] * (amount)
        for coin in coins:
            for num in range(1, amount+1):
                if num >= coin:
                    dp[num] += dp[num-coin]
        
        return dp[-1]