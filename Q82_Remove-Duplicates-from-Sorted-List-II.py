# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if head is None:
            return None
        
        dummy_head = dummy_node = ListNode(None)
        pre_node, node = head, head.next
        pre_val = head.val
        while node:
            if node.val == pre_val:
                pre_node = None
            else:
                if pre_node:
                    dummy_node.next = pre_node
                    dummy_node = pre_node
                    dummy_node.next = None
                pre_node = node
                pre_val = node.val
            node = node.next
        if pre_node:
            dummy_node.next = pre_node
            

        return dummy_head.next