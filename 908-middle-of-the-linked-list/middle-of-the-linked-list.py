# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        """
        intializing slow,fast pointers
        loop  over fast , fast next 
        return slow (mid)
        
        """
        slow=head
        fast=head


        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    

        
# T;O(n)
# S:O(1)