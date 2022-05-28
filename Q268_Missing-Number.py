class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (1+n)*n/2
        for num in nums:
            total -= num
        return int(total)