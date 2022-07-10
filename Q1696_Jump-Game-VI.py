class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-float('inf')]*len(nums)
        if len(nums) == 0:
            return 0
        dp[0] = nums[0]
        q = [(-dp[0], 0)]
        for idx in range(1, len(nums)):
            num = nums[idx]
            while q and q[0][1] < idx-k:
                heapq.heappop(q)
            dp[idx] = num-q[0][0]
            heapq.heappush(q, (-dp[idx], idx))
        return dp[-1]