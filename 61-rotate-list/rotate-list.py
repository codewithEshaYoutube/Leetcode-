# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next  or k==0:
            return head

        #step 1  find out length of link list , figur out tail
        length=1

        tail=head
        
        while tail.next:
            tail=tail.next
            length+=1
        # 2 making it circular
        tail.next=head

        # updating new tail new head
        k =k % length
        new_tail=head
        for i in range(length -k-1):

            new_tail=new_tail.next

        new_head=new_tail.next
        #breaking the circle

        new_tail.next=None
        return new_head
        

        
