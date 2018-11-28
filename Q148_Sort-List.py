# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        heap = []
        node = head
        idx = 0
        while node:
            heapq.heappush(heap, (node.val, idx, node))
            idx += 1
            node = node.next
            
        _, _, head = heapq.heappop(heap)
        pre_node = head
        while heap:
            _, _, node = heapq.heappop(heap)
            if pre_node:
                pre_node.next = node
            pre_node = node
        pre_node.next = None
        return head
        