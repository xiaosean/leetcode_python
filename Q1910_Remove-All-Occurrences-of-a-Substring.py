class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stacks = []
        check_n = len(part)
        for char in s:
            stacks += [char]
            if "".join(stacks[-check_n:]) == part:
                stacks = stacks[:-check_n]
        return "".join(stacks)
        