# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        cur = 0
        node = head
        while node:
            if node.val == 0:
                if cur:
                    res += [cur]
                cur = 0
            cur += node.val
            node = node.next
        node = dummy = ListNode()
        for num in res:
            node.next = ListNode(num)
            node = node.next
        return dummy.next