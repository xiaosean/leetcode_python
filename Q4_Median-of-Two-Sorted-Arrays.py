class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num_list = []
        nums1_gen = (num for num in nums1)
        nums2_gen = (num for num in nums2)

        #     list empty check
        if len(nums1) == 0:
            num_list = nums2
            return self.get_median_num(num_list)
        if len(nums2) == 0:
            num_list = nums1
            return self.get_median_num(num_list)
        num1 = next(nums1_gen)
        num2 = next(nums2_gen)
        
    #     generator iteration insert
        while True:
            if num1 <= num2:
                num_list += [num1]
                try:
                    num1 = next(nums1_gen)
                except StopIteration:
                    num_list += [num2] + [num for num in nums2_gen]
                    break
            else:
                num_list += [num2]
                try:
                    num2 = next(nums2_gen)
                except StopIteration:
                    num_list += [num1] + [num for num in nums1_gen] 
                    break

        return self.get_median_num(num_list)

    def get_median_num(self, nums):
    #     get mdeian num if odd return Xn/2 ; if even return (Xn/2 + X(n/2+1)) /2
        list_length = len(nums)
        if list_length % 2 == 1:
            return nums[int((list_length)/2)]
        else:
            return (nums[int((list_length-1)/2)] + nums[int((list_length-1)/2)+1])/2