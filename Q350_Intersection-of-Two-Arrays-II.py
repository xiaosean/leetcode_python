from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1
        num1_ctr = Counter(nums1)
        num2_ctr = Counter(nums2)
        intersect_l = []
        for i in num1_ctr:
            if i in num2_ctr:
                intersect_l += [i] * min(num1_ctr[i], num2_ctr[i])
        return intersect_l