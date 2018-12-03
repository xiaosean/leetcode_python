class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = zero_count = 0
        while(pos < n):
            if nums[pos] == 0:
                zero_count += 1
            else:
                nums[pos-zero_count] = nums[pos]
            pos += 1
        for i in range(zero_count):
            nums[-1-i] = 0