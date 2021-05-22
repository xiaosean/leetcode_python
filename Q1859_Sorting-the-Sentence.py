class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        out = [None] * len(words)
        for word in words:
            idx = int(word[-1]) -1
            out[idx] = word[:-1]
        return " ".join(out)
        