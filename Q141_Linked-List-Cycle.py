# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        step_1_node = step_2_node = head
        while step_1_node is not None:
            for _ in range(2):
                if step_2_node.next is None:
                    return False
                step_2_node = step_2_node.next
                if step_1_node == step_2_node:
                    return True
            step_1_node = step_1_node.next
        return False