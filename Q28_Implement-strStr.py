class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle)-len(haystack)>0:
            return -1
        for idx, letter in enumerate(haystack[:len(haystack)-len(needle)+1]):
            if haystack[idx:idx+len(needle)] == needle:
                return idx
        return -1