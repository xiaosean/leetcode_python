class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        cnt = 0
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == k:
                cnt += 1
                l += 1
                r -= 1
            elif sum_ < k:
                l += 1
            else:
                r -= 1
        return cnt