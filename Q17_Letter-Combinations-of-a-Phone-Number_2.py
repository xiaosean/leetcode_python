class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        res = []
        if not digits:
            return res
        
        for letter in table[digits[0]]:
            combination = self.letterCombinations(digits[1:])
            if not combination:
                res += [letter]
            else:
                for l in combination:
                    res += [letter+l]
        return res
