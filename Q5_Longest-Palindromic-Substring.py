class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def checkPalindrome(s):
            """
            check string is palindrome, if true return count, else return 0
            :type s: str
            :rtype: int
            """
            list_s = list(s)
            if list_s == list_s[::-1]:
                return len(list_s)
            return 0

        # check empty string
        if len(s) == 0:
            return ""
        longest_s = s[0]
        longest_count = 1
        letter_idx = {}
        letter_set = set(list(s))
        for idx, letter in enumerate(s):
            letter_idx[letter] = letter_idx.get(letter, []) + [idx]

        for letter in letter_set:
            letter_list = letter_idx[letter]
            if len(letter_list) > 1:
                # iterator check the farest string
                for i in range(len(letter_list)-1):
                    for j in range(len(letter_list)-1, i, -1):
                        start_idx = letter_list[i]
                        end_idx = letter_list[j]+1
                        substring = s[start_idx:end_idx]

                        temp_longest_count = end_idx - start_idx
                        # early break
                        if(temp_longest_count < longest_count):
                            break
                        
                        # check substring palindrome
                        palindrome_count = checkPalindrome(substring)

                        if longest_count < palindrome_count:
                            longest_s = substring
                            longest_count = palindrome_count
                        # early break
                        if palindrome_count > 0:
                            break

        return longest_s
