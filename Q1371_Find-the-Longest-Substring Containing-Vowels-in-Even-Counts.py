class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dp = [[0]*5 for _ in range(len(s)+1)]
        VOWEL_ENUM = {"a":0, "e":1, "i":2, "o":3, "u":4}
        max_substring = 0
        visit = {"00000":0}
        for idx, letter in enumerate(s):
            dp[idx+1] = dp[idx].copy()
            if letter in VOWEL_ENUM:
                dp[idx+1][VOWEL_ENUM[letter]] += 1
                dp[idx+1][VOWEL_ENUM[letter]] = dp[idx+1][VOWEL_ENUM[letter]] % 2
                t = "".join(map(str, dp[idx+1]))
                if t not in visit:
                    visit[t] = idx+1
        res = 0
        for idx in range(len(s), -1, -1):
            t = "".join(map(str, dp[idx]))
            if t in visit:
                res = max(res, idx-visit[t])
        return res
            
