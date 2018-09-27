# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_numbers = int(self.nodeTraverse(l1)) + int(self.nodeTraverse(l2))
        return [int(x) for x in str(sum_numbers)[::-1]]
    
    def nodeTraverse(self, node):
        """
        :type node: ListNode
        :rtype: str
        """
        node_str = ""
        while node is not None:
            node_str = str(node.val) + node_str
            node = node.next
        return node_str
        