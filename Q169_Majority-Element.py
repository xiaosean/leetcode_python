from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        n = len(nums)
        for key, count in nums_counter.most_common():
            if count > n/2:
                return key
        return None