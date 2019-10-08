class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l_idx, r_idx = 0, len(s)-1
        l, r = s[l_idx], s[r_idx]
        while l_idx < r_idx:
            if l != r:
                sub_s = s[l_idx:r_idx+1]
                return sub_s[:-1] == sub_s[:-1][::-1] or sub_s[1:] == sub_s[1:][::-1]
            l_idx += 1
            r_idx -= 1
            l, r = s[l_idx], s[r_idx]
        return True