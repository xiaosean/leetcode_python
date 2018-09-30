# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_count = 0
        node = head
        while node:
            node = node.next
            list_count += 1
        n = list_count - n
        count = 0
        pre_node = node = head
        while count < n:
            pre_node = node
            if node.next:
                node = node.next
            else:
                node.next = None
            count += 1
        if n == 0:
            head = node.next
        else:
            pre_node.next = node.next
        
        return head