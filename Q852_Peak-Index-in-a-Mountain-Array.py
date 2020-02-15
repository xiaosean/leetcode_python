class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:
            return None
        return A.index(max(A))