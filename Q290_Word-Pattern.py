class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern and not s:
            return True
        words = s.split()
        if len(pattern) != len(words):
            return False
        word2pattern = {}
        pattern2word = {}
        for pattern, word in zip(pattern, words):
            if pattern in pattern2word and pattern2word[pattern] != word:
                return False
            if word in word2pattern and word2pattern[word] != pattern:
                return False
            pattern2word[pattern] = word
            word2pattern[word] = pattern
        return True
                
                
                
            
            