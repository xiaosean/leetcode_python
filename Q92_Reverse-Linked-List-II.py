# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        stack = []
        init_node = ListNode(None)
        init_node.next = head
        pre_node = node = init_node
        pos = 0
        while pos < n:    
            node = node.next
            pos += 1
            if pos >= m:
                stack += [node]
            else:
                pre_node = node
        last_node = node.next
        while stack:
            node = stack.pop()
            pre_node.next = node
            pre_node = node
        pre_node.next = last_node
        return init_node.next