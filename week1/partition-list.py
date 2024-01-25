# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ptr = head
        great ,less = None,None
        
        grt = None
        while ptr:
            if ptr.val <x:
                if less == None:
                    less = ptr
                    head = less
                    
                else:
                    less.next = ptr
                    less = ptr
            else:
                if great == None:
                    great = ptr
                    grt = great
                else:
                    great.next = ptr
                    great = ptr
            ptr= ptr.next
        if great:
            great.next = None
        if less:
            less.next = grt
            return head
        else:
            return grt
        