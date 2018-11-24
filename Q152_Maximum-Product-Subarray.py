class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0 
        max_product = nums[0]
        positive_num = None
        positive_num_2 = None
        negtive_num = None
        negtive_num_2 = None
        for num in nums:
            if num != 0:
                if positive_num:
                    positive_num *= num
                if negtive_num:
                    negtive_num *= num
                if positive_num_2:
                    positive_num_2 *= num
                if negtive_num_2:
                    negtive_num_2 *= num
                
                if positive_num is None and num > 0:
                    positive_num = num
                if negtive_num is None and num < 0:
                    negtive_num = num
                elif negtive_num_2 is None and num < 0:
                    negtive_num_2 = num
                if negtive_num and positive_num_2 is None and negtive_num_2 is None and num > 0:
                    positive_num_2 = num
                    
                max_product = max(max_product, positive_num, negtive_num, positive_num_2, negtive_num_2, num)
            else:
                positive_num = negtive_num = positive_num_2 = negtive_num_2 = None
                max_product = max(max_product, 0)
        return max_product