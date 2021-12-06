# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # save the second node as even head
        # for loop
        #   using varialbe save next node
        if not head:
            return None
        node = head
        even_head = head.next
        while(node):
            temp_node = node.next
            if temp_node:
                node.next = node.next.next
            node = temp_node
        node = head
        while(node.next):
            node = node.next
        node.next = even_head
        return head