class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        if len(s) > 0:
            max_count = 1
        else: #     empty string
            return max_count
        substring = s[0]

        for index in range(len(s)-1):
            if s[index+1] in substring:
                repeat_idx = substring.index(s[index+1])
                if len(substring)-1 > repeat_idx:
                    substring = substring[repeat_idx+1:] + s[index+1]
                else:
                    substring = s[index+1]
            else:
                substring += s[index+1]

            if(len(substring) > max_count):
                max_count = len(substring)
        return max_count