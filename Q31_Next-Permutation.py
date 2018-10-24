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
                    # swap
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        # check nums[i...n ]  
                        # e.g. [4,2,0,2,3,2,0] 
                        # after change => [4,2,0,3,2,2,0] 
                        # check [2, 2, 0] part get minimize solution => get [0, 2, 2]
                        # Finally get [4,2,0,3,0,2,2] 
                        permution_iter(nums, front=i+1)
                        return
            #  if it is a descending list, reverse
            step = int((len(nums)-front)/2)
            for i in range(step):
                nums[front+i], nums[end-i] = nums[end-i], nums[front+i]
        permution_iter(nums)