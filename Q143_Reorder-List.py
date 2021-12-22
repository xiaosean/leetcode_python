# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        node = head
        while node:
            l += [node]
            node = node.next
        offset = 0
        if len(l) % 2:
            offset += 1
        left, right = l[:len(l)//2+offset], l[len(l)//2+offset:][::-1]
        if len(left) > len(right):
            right += [None]
        last_y = None
        for x, y in zip(left, right):
            if last_y:
                last_y.next = x
            x.next = y
            last_y = y
        if last_y is not None:
            last_y.next = None        
        return head
