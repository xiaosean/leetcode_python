class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stacks = []
        for op in ops:
            if op == 'C':
                stacks.pop()
            elif op == 'D':
                stacks += [stacks[-1]*2]
            elif op == '+':
                stacks += [stacks[-1]+stacks[-2]]
            else:
                stacks += [int(op)]
        return sum(stacks)