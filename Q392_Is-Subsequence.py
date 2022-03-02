class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if not s :
            return True
        cnt = 0
        for letter in t:
            if letter == s[cnt]:
                cnt += 1
                if cnt == len(s):
                    return True
        return False