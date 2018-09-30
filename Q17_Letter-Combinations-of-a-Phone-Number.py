class Solution:
    mapping_table = {
        "2":["a", "b", "c"],
        "3":["d", "e", "f"],
        "4":["g", "h", "i"],
        "5":["j", "k", "l"],
        "6":["m", "n", "o"],
        "7":["p", "q", "r", "s"],
        "8":["t", "u", "v"],
        "9":["w", "x", "y", "z"]
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        r_list = []
        if (len(digits) == 0):
            return []
        digit = digits[0]
        if (len(digits) == 1):
            return self.mapping_table[str(digit)]

    #     combine
        for letter in self.mapping_table[str(digit)]:
                letter_combine_list = self.letterCombinations(digits[1:])
                for combine_idx in range(len(letter_combine_list)):
                    r_list += [letter + letter_combine_list[combine_idx]]
        return r_list
