class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        count = 0
        stack = [-1]
        for idx, letter in enumerate(s):
            if letter == '(':
                stack += [idx]
                count -= 1
            if letter == ')':
                count += 1
    
                if count == 1:
                    count = 0
                    stack = [idx]
                else:
                    stack.pop()

                if len(stack):
                    start = stack[-1]
                    l = max(l, idx-start)
        return l