class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 2:
            return 0
        heap = []
        for idx, num in enumerate(height):
            heapq.heappush(heap, (num, idx))

        water = 0
        hi, hi_id = heapq.nlargest(1, heap)[0]
        idx_traversed = [hi_id]
        for num, idx in heapq.nlargest(n, heap)[1:]:
            if idx in idx_traversed:
                continue
    
            if num == 0:
                break
            for x in range(min(hi_id, idx)+1, max(hi_id, idx)):
                if num - height[x] >= 0:
                    water += num - height[x]
                    height[x] = num
                    idx_traversed += [x]

            hi, hi_id = num, idx
        return water
    