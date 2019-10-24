class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        new_s = ""
        for idx, s in enumerate(S):
            if s.isalpha():
                stack += [s]
        old_s = list(S)
        for idx, s in enumerate(S):
            if s.isalpha():
                old_s[idx] = stack.pop()
        return "".join(old_s)