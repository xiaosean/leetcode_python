class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        medium = nums[len(nums)//2]
        return sum([abs(num-medium) for num in nums])