class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is "":
            return ""
        n = len(s)
#         start by num
        if s[0].isdigit():
            pos = s.find("[")
            end_pos = pos
            stack = [True]
            while stack:
                end_pos += 1
                if s[end_pos] == '[':
                    stack += [True]
                elif s[end_pos] == ']':
                    stack.pop()
            num = int(s[:pos])
            return num*self.decodeString(s[pos+1:end_pos]) + self.decodeString(s[end_pos+1:])
#         start by letter
        else:
            substr = ""
            for index, letter in enumerate(s):
                if letter.isdigit():
                    return substr + self.decodeString(s[index:])
                if letter == ']':
                    return substr        
                substr += letter
            return substr