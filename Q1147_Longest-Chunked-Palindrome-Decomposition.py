class Solution:
    def longestDecomposition(self, text: str) -> int:
        l = 0
        r = len(text)-1
        l_stack = []
        r_stack = []
        count = 0
        while r > l:
            l_stack += [text[l]]
            r_stack += [text[r]]
            l_stack.sort()
            r_stack.sort()
            if l_stack == r_stack:
                count += 2
                l_stack = []
                r_stack = []
            r -= 1
            l += 1
        if r-l == 0 or l_stack:
            count += 1
            
        return count