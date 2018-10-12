class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #         two pass solution
        ans = [0, 0, 0]
        for num in nums:
            ans[num] += 1
        base_i = 0
        for idx, num in enumerate(ans):
            for i in range(num):
                nums[base_i+i] = idx
            base_i += num
