class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Space complexity O(amount)
        # Time complexity O(amount * the number of coins)
        # Using Dynamic programinig with bottom-up strategy
        # First, allocate the storage
        dp = [amount + 1] * (amount + 1)
        # Initialize the 0th dp to 0
        dp[0] = 0
        # Second. trace each number in the range of amount
        for num in range(amount+1):
            for coin in coins:
                # if this number can combine other coins and get the minimum value, replace to the dp[num]
                if num - coin >= 0:
                    dp[num] = min(dp[num], dp[num-coin]+1)
        # means didn't match any coins
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]