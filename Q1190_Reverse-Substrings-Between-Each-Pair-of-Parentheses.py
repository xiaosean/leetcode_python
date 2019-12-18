class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stacks = list
        # for each letter
        #   if '(':
        #        stack recording string => new_s
        #   elif ')':
        #        reverse new_s and concat the topest string of stack.
        #   else:
        #       append the letter to new_s
        stacks = [""]
        for letter in s:
            if letter == "(":
                stacks += [""]
            elif letter == ")":
                s = stacks.pop()
                stacks[-1] += s[::-1]
            else:
                stacks[-1] += letter
        return stacks[0]