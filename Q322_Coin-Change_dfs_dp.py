class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Space complexity O(amount)
        # Time complexity O(amount * the number of coins)
        # Using Dynamic programinig with dfs strategy
        # dfs:
        # for each coin
        #   if dp[num - coin] exists: it means the coins are possible to change, calculate the number of count when it is less than currently solution
        #   else: dfs() divide to minimum value to check is it possible to change the coins
        traverse_dp = {
            0: True
        }
        def coinChange_(num):
            # if the number already traverse
            if traverse_dp.get(num, False):
                return dp[num]
            # traverse each coin
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min(dp[num], coinChange_(num-coin)+1)
            # Record it has been traversed
            traverse_dp[num] = True
            return dp[num]
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        coinChange_(amount)
        return dp[-1] if dp[-1] < amount + 1 else -1
        
        