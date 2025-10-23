# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        initializing curr pointer
        loop until curr and curr.next gotout of balannce
        conditional comparing current value and next
        curr--->curr.next.next
        return head
        """
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next   #  skipping /deleting the node
            else:
                curr=curr.next
        return head
#T:O(N)
#S:O(1)
