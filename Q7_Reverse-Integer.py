class Solution:
    def reverse(self, x: 'int') -> 'int':
        s = str(x)[::-1]
        if x < 0:
            s = '-'+ s[:-1]
        int_s = int(s)
        if len(s) < 8:
            return int(s)
        int_s = int(s)
        if int_s > 2**31-1 or int_s < -2**31:
            return 0
        return int(s)