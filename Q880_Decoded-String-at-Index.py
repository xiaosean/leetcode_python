class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:

        s , count = [], 0
        for c in S:
            s += [c]
            if c.isdigit():
                count *= int(c)
            else:
                count += 1
            if count > K-1:
                break
        
        for c in reversed(s):
            K %= count
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                count /= int(c)
            else:
                count -= 1            
        return ""