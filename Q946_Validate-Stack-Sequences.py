class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stacks = []
        for num in pushed:
            stacks += [num]
            while stacks and popped and stacks[-1] == popped[0]:
                stacks.pop()
                del popped[0]
        return len(stacks)==0 and len(popped)==0
        