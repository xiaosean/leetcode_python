class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Dfs solution by traversing the word
        dp_ = [0] * (len(s)+1)
        keys = wordDict
        keys.sort()
        # print(keys)
        set_words = set("".join(wordDict))
        set_s = set(s)
        # Remove duplicated
        for letter in set_s:
            if letter not in set_words:
                return False
        def word_search(idx,res = []):
            if idx == len(s):
                res = [True]
                return res
            for key in keys:
                end_idx = idx+len(key)
                if end_idx <= len(s) and dp_[end_idx] == 0 and s[idx:end_idx] == key:
                    dp_[end_idx] = 1
                    res = word_search(end_idx, res)
                    if res:
                        return True
            return False
        return word_search(0)
                    
                