class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)-1
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, r]