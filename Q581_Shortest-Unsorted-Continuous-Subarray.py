class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sort_nums = nums.copy()
        sort_nums.sort()
        nums_order = [nums[i]==sort_nums[i] for i in range(n)]
        if all(nums_order):
            return 0
        else:
            invaild_pos = [idx for idx, flag in enumerate(nums_order) if not flag]
            return invaild_pos[-1]-invaild_pos[0]+1