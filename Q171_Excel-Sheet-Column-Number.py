class Solution:
    def titleToNumber(self, s: str) -> int:
        eng_dict = {chr(i):i-65+1 for i in range(65, 65+26)}
        idx = 0
        n = len(s)
        for i in range(1, n+1):
            num = eng_dict[s[-i]] * 26**(i-1)
            idx += num
        return idx