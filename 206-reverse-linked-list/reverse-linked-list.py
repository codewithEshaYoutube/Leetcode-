# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            # Save next node
            next_node = curr.next  
            
            # Reverse the pointer
            curr.next = prev  
            
            # Move forward
            prev = curr
            curr = next_node

        return prev
