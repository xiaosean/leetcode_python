class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp_p_list = [[1]]
        for _ in range(n*2-1):
            current_list = []
            for p in temp_p_list:
                for num in [1, -1]:
                    temp_p = p + [num]
                    if sum(temp_p) >= 0:
                        current_list += [temp_p]
            temp_p_list = current_list

    #     post-process 1=>'('  -1=>')'
        current_list = temp_p_list
        r_list = []
        for r in current_list:
    #         check Parenthesis consistent
            if sum(r) == 0:
                r = ['(' if x == 1 else ')'for x in r ]
                r_list += ["".join(r)]
        return r_list