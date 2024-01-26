# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev = head,None
        while curr :
            prev = curr
            curr = curr.next
            if  curr and curr.val == prev.val:
                while curr and  curr.val == prev.val:
                    curr = curr.next
                prev.next = curr

            
        return head

        