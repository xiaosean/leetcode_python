from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odd_flag = False
        count = 0
        for key, val in sorted(c.items(), key=lambda x:x[1], reverse=True):
            # print("key, val", key, val)
            if val % 2 > 0:
                if odd_flag:
                    val -= 1
                else:
                    odd_flag = True
            count += val
        return count