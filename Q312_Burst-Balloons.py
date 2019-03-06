class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = self.n = len(nums)
        if n < 3:
            return 0
        self.nums = nums
        self.dp_ = [[0]*n for i in range(n)]
        return self._maxCoins_helper(1, n-2)
    
    
    def _maxCoins_helper(self, start=0, end=0) -> int:
        if start > end:
            return 0
        if self.dp_[start][end] > 0:
            return self.dp_[start][end]
        for i in range(start, end+1):
            self.dp_[start][end] = max(self.dp_[start][end], \
                                       self._maxCoins_helper(start, i-1) + \
                                       self.nums[start-1] * self.nums[i] * self.nums[end+1] +\
                                       self._maxCoins_helper(i+1, end))
        return self.dp_[start][end]
        