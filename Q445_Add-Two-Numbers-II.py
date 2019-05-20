# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = None
        node1_stack = []
        node2_stack = []
        node1, node2 = l1, l2
        while True:
            if node1:
                node1_stack += [node1]
                node1 = node1.next
            if node2:
                node2_stack += [node2]
                node2 = node2.next
            if node1 is None and node2 is None:
                break
        if len(node2_stack) > len(node1_stack):
            node1_stack, node2_stack = node2_stack, node1_stack
        n, m = len(node1_stack), len(node2_stack)
        leading = 0
        for i in range(1, n+1):
            node1 = node1_stack[-i]
            if i <= m:
                node2 = node2_stack[-i]
                node1.val += node2.val + leading
            else:
                node1.val += leading
            leading = 0
            if node1.val >= 10:
                leading = node1.val // 10
                node1.val %= 10
        if node1_stack:
            if leading:
                new_node = ListNode(leading)
                new_node.next = node1_stack[0]
                return new_node
            return node1_stack[0]
        return None