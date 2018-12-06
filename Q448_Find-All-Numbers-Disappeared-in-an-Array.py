class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        disapper_list = [x for x in range(0, n+1)]
        for num in nums:
            disapper_list[num] = 0
            
        return [x for x in disapper_list if x > 0]