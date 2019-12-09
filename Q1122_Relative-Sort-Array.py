class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sort_key = {x:idx for idx, x in enumerate(arr2)}
        max_num = max(arr2)
        return sorted(arr1, key=lambda x:sort_key.get(x, max_num+x))