# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        current_node = headA
        link_a_count = 1
#         get head A linkedlist count
        headA_end = None
        while current_node.next != None:
            link_a_count += 1
            current_node = current_node.next
        headA_end = current_node
        
        link_b_count = 1
        current_node = headB
        while current_node.next != None:
            link_b_count += 1
            current_node = current_node.next
        
#       has intersection
        if current_node == headA_end:
            current_node_a = headA
            current_node_b = headB
#             move node to fair position which is same length to end
            if link_a_count > link_b_count:
                for _ in range(link_a_count-link_b_count):
                    current_node_a = current_node_a.next
            elif link_b_count:
                for _ in range(link_b_count-link_a_count):
                    current_node_b = current_node_b.next
            while current_node_a != current_node_b:
                current_node_a = current_node_a.next
                current_node_b = current_node_b.next
            return current_node_a
        
        return None