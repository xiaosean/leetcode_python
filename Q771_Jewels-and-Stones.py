class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        letter_count = {}
        for letter in S:
            letter_count[letter] = letter_count.get(letter, 0) + 1
        count = 0
        for letter in J:
            count += letter_count.get(letter, 0)
        return count
        