class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        offset1, offset2 = m-1, n-1
        while offset1 >= 0 and offset2 >= 0:
            num1, num2 = nums1[offset1], nums2[offset2]
            if num1 > num2:
                nums1[offset1+offset2+1] = num1
                offset1 -= 1
            else:
                nums1[offset1+offset2+1] = num2
                offset2 -= 1
        for i in range(offset2+1):
            nums1[i] = nums2[i]
        