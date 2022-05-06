class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k <= 1:
            return ""
        stacks = []
        for letter in s:
            if stacks and letter == stacks[-1][0]:
                stacks[-1][1] += 1
                if stacks[-1][1] == k:
                    stacks.pop()
            else:
                stacks += [[letter, 1]]
        res = ""
        for letter, cnt in stacks:
            res += letter*cnt
        return res