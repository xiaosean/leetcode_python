class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return None
        res = [nums[0]]
        for idx in range(1, len(nums)):
            res += [res[-1] + nums[idx]]
        return res