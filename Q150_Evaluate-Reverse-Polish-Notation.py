 class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacks = []
        while len(stacks) > 1 or tokens:
            if tokens:
                stacks += [tokens[0]]
                tokens = tokens[1:]
            
            last_token = stacks[-1]
            
            if last_token in ["+", "-", "*", "/"]:
                notation = str(stacks.pop())
                num2 = str(stacks.pop())
                num1 = str(stacks.pop())
                math_str = "".join([num1, notation, num2])
                res = int(eval(math_str))
                stacks += [res]

            
        return stacks[0]