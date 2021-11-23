class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Space complexity O(amount)
        # Time complexity O(amount * the number of coins)
        # Using Dynamic programinig with dfs strategy
        # dfs:
        # for each coin
        #   if dp[num - coin] exists: it means the coins are possible to change, calculate the number of count when it is less than currently solution
        #   else: dfs() traverse the small value to check whether the coins can be changed until reaching value 0 
        @lru_cache(None)
        def dp(num):
            if num == 0:
                return 0
            if num < 0:
                return float('inf')
            return min(dp(num - coin) for coin in coins) +1
        res = dp(amount)
        return res if res <= amount else -1