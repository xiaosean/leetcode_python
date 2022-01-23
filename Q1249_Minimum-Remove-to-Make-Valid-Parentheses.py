class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stacks = []
        for idx, letter in enumerate(s):
            if letter == ')':
                if stacks:
                    stacks.pop()
                else:
                    s[idx] = ''
            elif letter == '(':
                stacks.append(idx)
        while stacks:
            s[stacks.pop()] = ""
        return "".join(s)