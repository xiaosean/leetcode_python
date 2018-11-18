# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        step_1_node = step_2_node = head
        cycle_flag = False
        while step_1_node is not None:            
            
            step_1_node = step_1_node.next
            for _ in range(2):
                if step_2_node is None:
                    return None
                step_2_node = step_2_node.next
                
            if step_1_node == step_2_node:
                cycle_flag = True
                break
                
        if not cycle_flag:
            return None
        
#         already know having cycle
        while head is not step_1_node:
            head = head.next
            step_1_node = step_1_node.next
        return head