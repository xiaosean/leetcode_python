class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 pointer solution
        i = 0
        white = 0
        blue = len(nums)-1
        while i <= blue:
            if nums[i]  == 2:
                nums[i], nums[blue] = nums[blue], 2
                blue -= 1
                continue
            elif nums[i]  == 0:
                nums[i], nums[white] = 1, 0
                white += 1
            i += 1
        
