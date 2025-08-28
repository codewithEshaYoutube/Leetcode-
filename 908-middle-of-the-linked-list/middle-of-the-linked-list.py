# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        setting up positions for fast and slow
        loop (fast and fast.next)
        slow move one time
        fast  move two time
        return slow
        """
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        # T : O(n)
        #S:O(1)

        
        