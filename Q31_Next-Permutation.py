class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 2:
            return
        end = len(nums)-1
        def permution_iter(nums, front=0):
            for i in range(end-1, front-1, -1):
                for j in range(end, i, -1):
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        permution_iter(nums, front=i+1)
                        return
            step = int((len(nums)-front)/2)
            for i in range(step):
                nums[front+i], nums[end-i] = nums[end-i], nums[front+i]
        permution_iter(nums)