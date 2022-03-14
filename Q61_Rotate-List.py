# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get Node_{k+1}
        # set Node_k.next = None
        # set endnode to fist
        node = head
        idx = 0
        end_node = None
        cnt = 0
        while node:
            end_node = node
            node = node.next
            cnt += 1
        if cnt == 0:
            return head
        k = k%cnt
        if k==0:
            return head
        node = head
        k = cnt-k
        next_node = head
        while node:
            idx += 1
            if idx == k:
                next_node = node.next
                node.next = None
                break
            node = node.next
        end_node.next = head
        return next_node