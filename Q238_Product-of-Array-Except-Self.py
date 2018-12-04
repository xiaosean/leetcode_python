class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        productions = []
        n = len(nums)
        if n == 0:
            return None
#         def recursiveProductExceptSelf(idx=0, previous_value=1):
#             nonlocal productions
#             if idx == n-1:
#                 productions = [previous_value]
#                 return nums[idx]
#             mutply_after_values = recursiveProductExceptSelf(idx+1, previous_value=nums[idx]*previous_value)
#             except_self = previous_value*mutply_after_values
#             productions = [except_self] + productions 
            
#             # productions += [previous_value*recursiveProductExceptSelf(nums[1:], value, previous_value)]
#             return nums[idx]*mutply_after_values
        
#         recursiveProductExceptSelf()
        productions = [nums[0]]
        for i in range(n-1):
            productions += [nums[i+1] * productions[i]]
        # print("front production", productions)
        p = 1
        for i in range(n-1, 0, -1):
            productions[i] = productions[i-1] * p
            p *= nums[i]
        productions[0] = p
            
        return productions