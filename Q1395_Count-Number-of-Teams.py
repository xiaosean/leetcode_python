class Solution:
    def numTeams(self, rating: List[int]) -> int:        
        def helper(rating):
            res = 0
            for i in range(1, len(rating)-1):
                l_cnt, r_cnt = 0, 0
                for l in range(0, i):
                    if rating[l] < rating[i]:
                        l_cnt += 1
                for r in range(i+1, len(rating)):
                    if rating[r] > rating[i]:
                        r_cnt += 1
                res += l_cnt*r_cnt
            return res
        return helper(rating)+helper(rating[::-1])