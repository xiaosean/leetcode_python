# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num_s = ""
        while head:
            num_s += str(head.val)
            head = head.next
        return int(num_s, 2)