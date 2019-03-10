# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head, else_head = ListNode(0), ListNode(0)
        less_node = less_head
        else_node = else_head

        node = head
        if node is None:
            return None
        while node:
            next_node = node.next
            # print(node.val)
            if node.val < x:
                less_node.next = node
                less_node = node
                less_node.next = None
            else:
                else_node.next = node
                else_node = node
                else_node.next = None
            node = next_node
            
        if less_head.next is None:
            return else_head.next
        less_node.next = else_head.next
        return less_head.next