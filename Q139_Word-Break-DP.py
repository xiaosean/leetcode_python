class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       # Using dp to solve this problem
       # Traverse each letter of string and trace each word can fit this situation or not
       # for each index of string
       #    for word in worddict
       #        combine dp
       #        if dp[idx-word_len] and s[idx-word_len:] == word:
       #            return true
    
        dp = [True] + [False] * len(s)
        for idx in range(len(s)):
            for word in wordDict:
                if idx+1-len(word) >= 0 and dp[idx+1-len(word)] and s[idx+1-len(word):idx+1] == word:
                    dp[idx+1] = True
                    break
        return dp[-1]
    