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
        ## Step1 find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ## Step2 reverse the half part
        head2 = slow.next
        prev, curr = None, head2
        while curr:
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_
        slow.next = None
        # Step3. Merge 2 list
        # clear the middle of path to avoid to a cycle
        head1, head2 = head, prev
        while head1 and head2:
            next1, next2 = head1.next, head2.next
            head1.next = head2
            head2.next = next1
            head1, head2 = next1, next2
        
        return head
            