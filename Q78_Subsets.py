class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def deep_subsets(nums):
            r = []
            n = len(nums)
            if n == 1:
                return [nums] 
            for idx, num in enumerate(nums):
                r += [[num]]
                for sb in deep_subsets(nums[idx+1:]):
                    r += [[num] + sb]

            return r
        r = [[]]
        r += deep_subsets(nums)
        return r
