# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while lists:
            min_value = None
            min_idxies = []
            for idx, x in enumerate(lists):
                if x is not None:   
                    if min_value is None or x.val < min_value:
                        min_idxies  = [idx]
                        min_value = x.val
#                 same value
                    elif x.val == min_value:
                        min_idxies  += [idx]

            if min_value is not None:
                first_index = min_idxies[0]
                node = head_node = lists[first_index]
                lists[first_index] = lists[first_index].next
                for idx in min_idxies[1:]:
                    node.next = lists[idx]
                    node = node.next
                    lists[idx] = lists[idx].next
                node.next = self.mergeKLists(lists)
                return head_node
            return None                
