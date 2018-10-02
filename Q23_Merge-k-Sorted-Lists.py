# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    import heapq
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        if lists:
            for idx, element in enumerate(lists):
                if element:
                    heapq.heappush(heap, (element.val, idx, element))
        head = cur_node = ListNode(0)
        while heap:
            _, idx, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            cur_node.next = node
            cur_node = cur_node.next
        return head.next