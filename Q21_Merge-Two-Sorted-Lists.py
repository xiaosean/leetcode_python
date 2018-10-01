# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        effcient version
        inspire from https://leetcode.com/problems/merge-two-sorted-lists/discuss/9713/A-recursive-solution
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if (l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
        # l1_node = l1
        # l2_node = l2
        # if l1_node is None:
        #     return l2_node
        # if l2_node is None:
        #     return l1_node
        
        # if l1_node.val < l2_node.val:
        #     merge_node = l1_node
        #     l1_node = l1_node.next
        # else:
        #     merge_node = l2_node
        #     l2_node = l2_node.next
                
        # merge_head = merge_node
        
        # while l1_node or l2_node:
        #     if l1_node is None:
        #         merge_node.next = l2_node
        #         merge_node = l2_node
        #         l2_node = l2_node.next
        #     elif l2_node is None:
        #         merge_node.next = l1_node
        #         merge_node = l1_node
        #         l1_node = l1_node.next
        #     else:
        #         if l1_node.val <= l2_node.val:
        #             merge_node.next = l1_node
        #             merge_node = l1_node
        #             l1_node = l1_node.next
        #         else:
        #             merge_node.next = l2_node
        #             merge_node = l2_node
        #             l2_node = l2_node.next
        # return merge_head