class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        s = s.upper()
        res = ""
        end = len(s)-1
        for idx in range(len(s)):
            if idx > 0 and idx%k == 0:
                res = "-" + res    
            res = s[end-idx] + res
        return res
            