# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        nodes = []
        node = head
        while node:
            nodes += [node]
            node = node.next
        n = len(nodes)
        if n < 1:
            return None
        for idx in range(1, n, 2):
            nodes[idx-1], nodes[idx] = nodes[idx], nodes[idx-1]
        last_node = None
        for node in nodes:
            if last_node:
                last_node.next = node
            last_node = node   
        nodes[-1].next = None
        return nodes[0]