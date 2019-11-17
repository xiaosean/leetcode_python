class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         elegant version
        # return [i for i in range(left, right+1) if all(j and i % j == 0 for j in map(int, str(i)))]
        # fast version beat 99%
        self_div_list = []
        for i in range(left, right+1):
            num = i
            success_flag = True
            while num > 0:
                div_num = num % 10
                if not div_num or i % div_num > 0:
                    success_flag = False
                    break
                num = num // 10
            if success_flag:
                self_div_list += [i]
        return self_div_list