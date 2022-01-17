class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        positive = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            positive = -1
        nums_str = "0"
        for letter in s:
            if "0" <= letter <= "9":
                nums_str += letter
            else:
                break
        num = positive*int(nums_str)
        if num > 2**31-1:
            return 2**31-1
        if num < -2**31:
            return -2**31
        
        return num
            