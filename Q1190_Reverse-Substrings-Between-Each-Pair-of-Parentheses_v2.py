class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for letter in s:
            if letter == '(':
                stack += [""]
            elif letter == ')':
                reverse_str = stack.pop()[::-1]
                stack[-1] += reverse_str
            else:
                stack[-1] += letter
        return stack[-1]