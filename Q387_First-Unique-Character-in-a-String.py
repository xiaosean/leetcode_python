from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for index, char in enumerate(s):
            if c[char] == 1:
                return index
        return -1