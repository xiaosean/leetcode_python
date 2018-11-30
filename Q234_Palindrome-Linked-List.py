# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True
            
        node = head
        count = -1
        while node:
            node = node.next
            count += 1
        node = head
        
        mid_count = int((count+1)/2)
        pre_node = None
        for _ in range(mid_count):
#             reverse
            next_node = node.next
            node.next = pre_node    
            pre_node = node
            node = next_node
            
        reverse_node = pre_node
        if count % 2 == 1:
            middle_node = node
        else:
            middle_node = node.next

        node_from_mid = middle_node
        while node_from_mid:
            if node_from_mid.val != reverse_node.val:
                return False
            reverse_node = reverse_node.next
            node_from_mid = node_from_mid.next
            
        return True