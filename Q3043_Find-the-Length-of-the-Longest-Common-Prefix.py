class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        seen = set()
        for arr in arr1:
            s = str(arr)
            for i in range(len(s)):
                seen.add(s[:i+1])
        for arr in arr2:
            s = str(arr)
            for i in range(len(s)-1, -1, -1):
                if i < res:
                    break
                if s[:i+1] in seen:
                    res = max(res, i+1)
                    break
        return res
