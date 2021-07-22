class Solution:
    def pushDominoes(self, dominoes: str) -> str:
#         In the sides, one way push
        # result = [None] * len(dominoes)
        result = ""
        stack = []
        r_flag = None
        for item in dominoes:
            n = len(stack)
            if item == ".":
                stack += ["."]
                
            if item == "L":
                if r_flag:
                    r_flag = False
                    result += "R" * (n//2)
                    if n % 2 == 1:
                        result += "."
                    result += "L" * (n//2)  
                else:
                    result += "L" * n
                result += "L"
                stack = []
                
            if item == "R":
                if r_flag:
                    result += "R" * n
                else:
                    result += "." * n
                    
                r_flag = True
                result += "R"
                stack = []
                
        n = len(stack)
        if r_flag:
            result += "R" * n
        else:
            result += "." * n    
        return result
