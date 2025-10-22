# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        dummy node
        curr intialize
        looping over
        curr value = val
        return dummy.next

        """
        dummy=ListNode(0)
        dummy.next=head
        # intializing curr
        curr=dummy
        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next
        #T:O(n)
        #S:O(1)