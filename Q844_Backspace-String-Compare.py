class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
#         for each_str <= [S, T]
    #         empty stack
    #         for each letter
    #             if equals #:
    #                 delete last letter
    #             else:
    #                 append letter
#              transform stack to string 
#           compare each_str is equal or not
        res = []
        for each_str in [S, T]:
            stacks = []
            for letter in each_str:
                if letter == "#":
                    if stacks:
                        stacks.pop()
                else:
                    stacks.append(letter)
            res.append("".join(stacks))
        return res[0] == res[1]