# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin_node, end_node = None, None
        cnt = 0
        slow = fast = head
        for i in range(k):
            begin_node = fast
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        end_node = slow
        begin_node.val, end_node.val = end_node.val, begin_node.val
        return head