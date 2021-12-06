class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if not position:
            return 0
        coins_list = [0] * 2
        for num in position:
            coins_list[num % 2] += 1
        return min(coins_list)