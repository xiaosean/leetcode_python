class Solution:
    def nextGreaterElement(self, n: int) -> int:
#         from end to start check ascending or not
#            if not:
#               means it can find a greater value by changing the posion
#               get the position
#               check the digits after that position
#               pick the smallest one and order others  
        MAX_INT = 2**31
        str_n = str(n)
        n_length = len(str(n))
        last = n % 10
        for i in range(n_length-2, -1, -1):
            num = int(str_n[i])
            if num < last:
                int_list = list(map(int, str_n[i:]))
                int_list.sort()
                for greater_num in int_list:
                    if greater_num > num:
                        min_val = greater_num
                        int_list.remove(min_val)
                        break
                str_n = str_n[:i] + str(min_val) + "".join(map(str, int_list))
                return int(str_n) if int(str_n) < MAX_INT else -1
            last = num
        return -1