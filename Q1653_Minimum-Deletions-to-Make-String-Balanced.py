class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        b_count = 0
        for i in s:
            if i == "a":
                res = min(res+1, b_count)
            else:
                b_count += 1
        return res