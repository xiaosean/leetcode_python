class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        if n == 0:
            return True
        for idx, flower in enumerate(flowerbed):
            if flower == 0:
                near = []
                if idx < len(flowerbed)-1:
                    near += [flowerbed[idx+1]]
                if idx > 0:
                    near += [flowerbed[idx-1]]
                if sum(near) == 0:
                    cnt += 1
                    flowerbed[idx] = 1
                    if cnt == n:
                        return True
        return False
                    
                
                