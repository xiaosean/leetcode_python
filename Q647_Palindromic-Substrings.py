class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        count = 0
        n = len(s)
        def check_palindromic(input):
            return input == input[::-1]
                 
        for i in range(n):
            for j in range(i, n):
                count += check_palindromic(s[i:j+1])
        return count