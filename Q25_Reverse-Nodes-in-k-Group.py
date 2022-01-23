# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step1. save the postion i-1
        # from i index and look forward k node
        # if exists:
        #    swap and set up the i-1 node to point the i
        # Step2. create a function to swap in k nodes
        if k == 1:
            return head
        node = dummy = ListNode(None, next=head)
        
        def next_k_node(head, k):
            cnt = 0
            node = head
            while node:
                cnt += 1
                if cnt == k:
                    return node
                node = node.next
            return None
        def swap_k_node(head, k):
            cnt = 0
            node = head
            last_node = None
            while node:
                next_node = node.next
                node.next = last_node
                last_node = node
                node = next_node
                cnt += 1
                if cnt == k:
                    return last_node
            return None
        
        while node:
            next_beginning = None
            next_node = node.next
            end_of_k = next_k_node(next_node, k)
            if end_of_k:
                next_beginning = end_of_k.next
                node.next = swap_k_node(next_node, k)
                next_node.next = next_beginning
                node = next_node
            else:
                break
        return dummy.next
            
        