# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        slow,fast
        reverse
        check on each pointer position
        """
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse
        prev=None
        while slow:
            temp=slow.next 
            slow.next=prev
            prev=slow
            slow=temp
        # two pointers
        left,right=head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
#T:O(n)
#S: O(1)



        
