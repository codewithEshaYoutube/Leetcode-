# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        two pointes
        curr
        prev
        loop for curr
        pointers update
        temp pointer
        return prev

        """
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
