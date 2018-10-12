class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1  
    #     all 1
        count = 0
    #     DP
        two_count = int(n / 2)
        one_count = n % 2
        while n >= one_count:
            x = two_count + one_count
            #     C n 2
            P_U = P_D = P_D2 = 1
            for i in range(1, x+1):
                P_U *= i
            for i in range(1, x+1-two_count):
                P_D *= i
            for i in range(1, two_count+1):
                P_D2 *= i
            count += int(P_U/(P_D*P_D2))
            two_count -= 1
            one_count += 2
        return count