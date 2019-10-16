from collections import Counter
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        c = Counter(s)
        for key, value in c.items():
            if value == 1:
                return False
            for v in range(value, 1, -1):
                substr = s[:n // v]
                multsubstr = substr * v
                if multsubstr == s:
                    return True
            return False
        