class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r_size = c_size = 0
        if nums:
            r_size = len(nums)
            if r_size > 0:
                c_size = len(nums[0])
        if r_size*c_size != r*c:
            return nums
        else:
            flatten = [nums[i][j] for i in range(r_size) for j in range(c_size)]
            resize_nums = []
            for i in range(r):
                resize_nums += [flatten[i*c:(i+1)*c]]
            return resize_nums