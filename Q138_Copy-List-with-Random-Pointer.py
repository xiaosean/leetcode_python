"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ori_list, cpy_list = [], []
        hashtable = {}
        node = head
        idx = 0
        while node:
            val, rand = node.val, node.random
            hashtable[node] = idx
            cpy_node = ListNode(val)
            if cpy_list:
                cpy_list[-1][0].next = cpy_node
            cpy_list += [(cpy_node, rand)]
            node = node.next
            idx += 1
        for node, rand in cpy_list:
            idx = hashtable[rand] if rand else None
            node.random = cpy_list[idx][0] if rand else None
        return cpy_list[0][0] if cpy_list else None