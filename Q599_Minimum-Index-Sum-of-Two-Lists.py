class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_table = {key: idx for idx, key in enumerate(list1)}
        list2_table = {key: idx for idx, key in enumerate(list2)}
        if len(list1_table) > len(list2_table):
            list1_table, list2_table = list2_table, list1_table
        min_val, min_key = len(list1)+len(list2)+1, None
        for key in list1_table:
            if key in list2_table:
                least_idx_sum = list1_table[key] + list2_table[key]
                if least_idx_sum < min_val:
                    min_val = least_idx_sum
                    min_key = [key]
                elif least_idx_sum == min_val:
                    min_key += [key]
        return min_key