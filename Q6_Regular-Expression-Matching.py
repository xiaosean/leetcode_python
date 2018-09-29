class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = re.compile(p)        
        if pattern.fullmatch(s):
            return True
        return False