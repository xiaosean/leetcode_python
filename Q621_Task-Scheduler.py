from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        
        if n == 0:
            return len(tasks)
        
        cost = 0
        heap = []
        c = Counter(tasks)
        for key, val in c.items():
            heapq.heappush(heap, (-val, key))
        
        while heap:
            temp = []
            for _ in range(n+1):
#                 run task
                if heap:
                    cost += 1
                    val, key = heapq.heappop(heap)
                    if val < -1:
                        temp += [(val+1, key)]
#                 idle
                elif len(temp)>0:
                    cost += 1
                else:
                    break
            for val, key in temp:
                heapq.heappush(heap, (val, key))
                
        return cost