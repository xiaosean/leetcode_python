class Solution:
    def threeSum(self, nums):
        """
        inspired from https://leetcode.com/problems/3sum/discuss/169885/Python-or-tm
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sum_zero_list = []
        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                continue
            l_pos, r_pos = idx+1, len(nums)-1

            while l_pos < r_pos:
                sum_ = num + nums[l_pos] + nums[r_pos]
                if num + nums[l_pos] + nums[r_pos] == 0:
                    zero_sum = [nums[l_pos], num, nums[r_pos]]
    #                 if zero_sum not in sum_zero_list:
                    sum_zero_list += [zero_sum]
                    # if match it will not match others number
                    l_pos += 1
                    r_pos -= 1
    #                 accelerate
                    while r_pos > l_pos and nums[l_pos] == nums[l_pos - 1]: 
                        l_pos += 1
                    while r_pos > l_pos and nums[r_pos] == nums[r_pos + 1]: 
                        r_pos -= 1
                else: 
                    if sum_ > 0: 
                        r_pos -= 1
                    else:
                        l_pos += 1
        return sum_zero_list