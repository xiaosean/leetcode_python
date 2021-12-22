# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        dummy = ListNode(0)
        sort_node = dummy
        slow, fast = head, head.next
        while fast:
            # duplicated
            if fast.val == slow.val:
                while fast and fast.val == slow.val:
                    fast = fast.next
                if not fast:
                    sort_node.next = None
                    return dummy.next
            else:
                sort_node.next = slow
                sort_node = sort_node.next
            slow = fast
            fast = fast.next
        sort_node.next = slow
        return dummy.next