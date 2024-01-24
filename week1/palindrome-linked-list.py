# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast ,pslow= head,head,None
        l = head
        while fast and fast.next:
            pslow = slow
            slow = slow.next
            fast = fast.next.next
        
        if pslow:
            pslow.next = None
        
        curr,prev = slow,None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        while l and prev :
            if l.val != prev.val:
                return False
            l = l.next
            prev = prev.next
        return True
        