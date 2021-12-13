class Solution:
    def maxPower(self, s: str) -> int:
        prev = ""
        max_cnt, cnt = 1, 0
        for letter in s:
            if letter == prev:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
                prev = letter
        return max_cnt