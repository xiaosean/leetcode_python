class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num2 = num2.zfill(len(num1))
        c = 0
        add_str = ""
        for i in range(len(num1)-1, -1, -1):
            digit_1 = int(num1[i])
            digit_2 = int(num2[i])
            digit = digit_1 + digit_2 + c
            c = digit // 10
            digit = digit % 10
            add_str = str(digit) + add_str
        if c:
            add_str = str(c) + add_str
        return add_str