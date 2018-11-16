class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words_table = {}
        def wordBreakIter(s, wordDict):
            if len(s) == 0:
                return True
            if s in words_table:
                return words_table[s]
            for word in wordDict:
                word_n = len(word)
                truncate_str = s[:word_n]
                if truncate_str == word:
                    if wordBreakIter(s[word_n:], wordDict):
                        words_table[s] = True
                        return True
                words_table[s] = False
            return False
        # remove combination words
        if not set(s).issubset(set("".join(wordDict))):
            return False
        wordDict.sort(reverse=True, key=lambda n: len(n))
        return wordBreakIter(s, wordDict)
