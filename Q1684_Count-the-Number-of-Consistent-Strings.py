class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        unique_chars = set(allowed)
        cnt = 0
        for word in words:
            cnt += 1
            for letter in word:
                if not letter in unique_chars:
                    cnt -=1
                    break
            
        return cnt