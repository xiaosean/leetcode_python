class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            for count in range(2):
                for i in range(len(stones)-count):
                    stone = stones[i + count]
                    if stone > stones[count]:
                        stones[i + count], stones[count] = stones[count], stones[i + count]    
            if stones[0] == stones[1]:
                stones = stones[2:]
            else:
                stones = stones[2:] + [stones[0] - stones[1]]
        if stones:
            return stones[0]
        return 0