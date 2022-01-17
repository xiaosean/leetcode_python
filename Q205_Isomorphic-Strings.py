class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(s)==len(t) and len(set(s))==len(set(t))==len(set(zip(s, t)))