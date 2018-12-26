class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hamming = [int(digit) for digit in bin(x ^ y)[2:]] #0bxxxx
        return sum(hamming)