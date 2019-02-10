class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
#         solution from:https://leetcode.com/problems/queue-reconstruction-by-height/discuss/167308/Python-solution
        # print(people)
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        # print(people)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res