class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_start = ['(', '{', '[']
        parentheses_end = [')', '}', ']']
        parentheses_end_mapping = {
            ")":"(",
            "}":"{",
            "]":"[",

        }
        parentheses_stack = []
        for idx, letter in enumerate(s):
            if letter in parentheses_start:
                parentheses_stack += [letter]
            elif letter in parentheses_end:
                if len(parentheses_stack) > 0:
                    if parentheses_stack[-1] != parentheses_end_mapping[letter]:
                        return False
                    else:
                        parentheses_stack.pop()
                else:
                    return False
        if len(parentheses_stack) != 0:
            return False
        return True
            